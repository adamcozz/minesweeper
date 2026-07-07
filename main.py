from random import randint

class Board:
    
    #board constructor method to specify board width, height, and num of mines  
    def __init__(self, width = 10, height = 5, mines = 10):
        self.width = width
        self.height = height
        self.mines = mines
    
    #method to generate array of mines and numbers
    def hidden_board(self):
        
        #generate self.width x self.height array of 0s
        matrix = [["0" for i in range(self.width)] for i in range(self.height)]
        
        #randomly place self.mines x num of mines
        count = 0
        while count < self.mines:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            if matrix[y][x] != "B":
                matrix[y][x] = "B"
                count += 1
        
        #populate array with numbers that correspond to num of adjacent mines
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
        
        #return self.width x self.height array populated with self.mines x num of mines and numbers that correspond to num of adjacent mines
        return matrix
    
    
    #method to generate an initial array to display to the user
    def display_board(self, hidden_matrix):
        
        #generate self.width x self.height array of ░
        matrix = [["░" for _ in range(self.width)] for _ in range(self.height)]
        
        #replace a ░ cell with a correpsonding cell from another array "hidden_matrix"
        while True:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            if hidden_matrix[y][x] != "B":
                matrix[y][x] = hidden_matrix[y][x]
                break
        
        #return self.width x self.height array of ░ with a cell randomly replaced by a corresponding cell from another array
        return matrix

class Game:
    
    #game constructor method to specify game status and game baord
    def __init__(self):
        self.game_over = False
        self.game_board = Board()
        self.hidden_matrix = self.game_board.hidden_board()
        self.display_matrix = self.game_board.display_board(self.hidden_matrix)
    
    #method to convert array to multi line string to print
    def render_board(self):
        
        #genertate strings of each row in game board array and add a row label to show coordinate system
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        rows = []
        for i in range(self.game_board.height):
            row_label = alphabet[i]
            row_string = row_label + ''.join(map(str, self.display_matrix[i]))
            rows.append(row_string)
        
        #add a string to be displayed at the top of the multi line sting to show coordinate system
        rows.insert(0, " " + alphabet[:self.game_board.width])
        
        #print multi line string of all rows
        print("\n".join(rows))
    
    
    #method for user to select and replace a cell from the displayed array
    def move(self, coordinates=None):
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        #validate user coordinate input - if nothing input, get user to enter coordinates
        if coordinates is None:
            coordinates = input("Enter coordinates (pick row, then column. e.g. 'dc'): ")
        
        #validate user coordinate input - check if more than two characters were entered
        if len(coordinates) != 2:
            print("Invalid input. Enter exactly two letters like 'dc'.")
            return

        #validate user coordinate input - ensure input is lowercase
        row_letter = coordinates[0].lower()
        col_letter = coordinates[1].lower()

        #validate user coordinate input - check if characters are in alphabet
        if row_letter not in alphabet or col_letter not in alphabet:
            print("Invalid input. Use letters only, e.g. 'dc'.")
            return

        #identify index of characters in alphabet and replace self.display_matrix cell with self.hidden_matrix cell
        y = alphabet.index(row_letter)
        x = alphabet.index(col_letter)
        self.display_matrix[y][x] = self.hidden_matrix[y][x]

        #call render_board() method to print new multi line string
        self.render_board()

    #method to start and run game
    def loop(self):
        
        #print initial multi line string
        self.render_board()
        
        #repeatedly call self.move method while win and loss conditons not met
        while not self.game_over:
            self.move()
            
            #create 1d array of all cells in display_matrix
            flat = [cell for row in self.display_matrix for cell in row]

            #end game if mine has been revealed
            if "B" in flat:
                print("Game over")
                self.game_over = True
            
            #end game if num of mines equals num of ░ cells
            if flat.count("░") == self.game_board.mines:
                print("You win!")
                self.game_over = True

#run game
game = Game()
game.loop()
