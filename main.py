from random import randint

class Board:
    def __init__(self, width = 10, height = 5, mines = 10):
        self.width = width
        self.height = height
        self.mines = mines
    
    #Function to generate hidden game board
    def hidden_board(self):
        
        #Generate width x height array of 0s
        matrix = [["0" for i in range(0, self.width)] for i in range(0, self.height)]

        #Populate array with mines in random positions
        count = 0
        while count < self.mines:   
            randnum_one = randint(0, self.width - 1)
            randnum_two = randint(0, self.height - 1)
            if matrix[randnum_two][randnum_one] != "B":
                matrix[randnum_two][randnum_one] = "B"
                count += 1
        
        #Populate array with numbers which correspond to number of adjacent mines
        conditions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1),  (1, 0), (1, 1)] 
        for i in range(0, self.height):
            for j in range(0, self.width):
                if matrix[i][j] == "B":
                    continue
                counter = 0
                for dy, dx in conditions:
                    ny = i + dy
                    nx = j + dx
                    if 0 <= ny < self.height and 0 <= nx < self.width:
                        if matrix[ny][nx] == "B":
                             counter += 1
                matrix[i][j] = counter
        
        return matrix
    
    #Function to display game baord
    def display_board(self):
        
        #Generate width x height array of ░
        matrix = [["░" for i in range(0, self.width)] for i in range(0, self.height)]
        
        #Display random item from hidden game board
        while True:
            randnum_one = randint(0, self.width - 1)
            randnum_two = randint(0, self.height - 1)
            hidden_item = self.hidden_board()[randnum_two][randnum_one]
            if hidden_item != "B":
                matrix[randnum_two][randnum_one] = hidden_item
                break

        #Create a multi line string to return
        board_string = '\n'.join(''.join(map(str,row))for row in matrix)
        
        return board_string
        
class Game:
    def __init__(self):
        return
    
board_one = Board()

print(board_one.display_board())