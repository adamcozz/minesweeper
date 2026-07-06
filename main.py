from random import randint

class Board:
    def __init__(self, width = 10, height = 5, mines = 10):
        self.width = width
        self.height = height
        self.mines = mines
    
    def hidden_board(self):
        matrix = [["0" for i in range(self.width)] for i in range(self.height)]
        count = 0
        while count < self.mines:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            if matrix[y][x] != "B":
                matrix[y][x] = "B"
                count += 1
        
        conditions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for y in range(self.height):
            for x in range(self.width):
                if matrix[y][x] == "B":
                    continue
                counter = 0
                for dy, dx in conditions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < self.height and 0 <= nx < self.width:
                        if matrix[ny][nx] == "B":
                            counter += 1
                matrix[y][x] = counter
        return matrix
    
    def display_board(self, hidden_matrix):
        matrix = [["░" for _ in range(self.width)] for _ in range(self.height)]
        while True:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            if hidden_matrix[y][x] != "B":
                matrix[y][x] = hidden_matrix[y][x]
                break
        return matrix

class Game:
    def __init__(self):
        self.game_over = False
        self.game_board = Board()
        self.hidden_matrix = self.game_board.hidden_board()
        self.display_matrix = self.game_board.display_board(self.hidden_matrix)
    
    def render_board(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        rows = []
        for i in range(self.game_board.height):
            row_label = alphabet[i]
            row_string = row_label + ''.join(map(str, self.display_matrix[i]))
            rows.append(row_string)
        rows.insert(0, " " + alphabet[:self.game_board.width])
        print("\n".join(rows))
    
    def move(self, coordinates=None):
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if coordinates is None:
            coordinates = input("Enter coordinates (pick row, then column. e.g. 'dc'): ")

        if len(coordinates) != 2:
            print("Invalid input. Enter exactly two letters like 'dc'.")
            return

        row_letter = coordinates[0].lower()
        col_letter = coordinates[1].lower()

        if row_letter not in alphabet or col_letter not in alphabet:
            print("Invalid input. Use letters only, e.g. 'dc'.")
            return

        y = alphabet.index(row_letter)
        x = alphabet.index(col_letter)

        self.display_matrix[y][x] = self.hidden_matrix[y][x]

        self.render_board()

    def loop(self):
        self.render_board()
        while not self.game_over:
            self.move()
            
            flat = [cell for row in self.display_matrix for cell in row]

            if "B" in flat:
                print("Game over")
                self.game_over = True
            
            if flat.count("░") == self.game_board.mines:
                print("You win!")
                self.game_over = True

game = Game()
game.loop()
