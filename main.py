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
        
        #Populate array with numbers which correspond to the number of mines adjacent to item in array
        for i in range(0, len(matrix)):
            #0th row conditions
            if i == 0:
                 for j in range(0, len(matrix[i])):
                    counter = 0
                    #Firts item in row conditons
                    if j == 0:
                        if matrix[i][j] == "B":
                            continue
                        if matrix[i][j + 1] == "B":
                            counter += 1
                        if matrix[i + 1][j] == "B":
                            counter += 1
                        if matrix[i + 1][j + 1] == "B":
                            counter += 1
                        matrix[i][j] = counter
                    #Last item in row conditions
                    elif j == len(matrix[i]) - 1:
                        if matrix[i][j] == "B":
                            continue
                        if matrix[i][j - 1] == "B":
                            counter += 1
                        if matrix[i + 1][j] == "B":
                            counter += 1
                        if matrix[i + 1][j - 1] == "B":
                            counter += 1
                        matrix[i][j] = counter
                    #Middle item in row conditions
                    else:
                        if matrix[i][j] == "B":
                            continue
                        if matrix[i][j - 1] == "B":
                            counter += 1
                        if matrix[i][j + 1] == "B":
                            counter += 1
                        if matrix[i + 1][j] == "B":
                            counter += 1
                        if matrix[i + 1][j - 1] == "B":
                            counter += 1
                        if matrix[i + 1][j + 1] == "B":
                            counter += 1
                        matrix[i][j] = counter
            #Final row conditions
            elif i == len(matrix) - 1:
                 for j in range(0, len(matrix[i])):
                    counter = 0
                    #Firts item in row conditons
                    if j == 0:
                        if matrix[i][j] == "B":
                            continue
                        if matrix[i][j + 1] == "B":
                            counter += 1
                        if matrix[i - 1][j] == "B":
                            counter += 1
                        if matrix[i - 1][j + 1] == "B":
                            counter += 1
                        matrix[i][j] = counter
                    #Last item in row conditions
                    elif j == len(matrix[i]) - 1:
                        if matrix[i][j] == "B":
                            continue
                        if matrix[i][j - 1] == "B":
                            counter += 1
                        if matrix[i - 1][j] == "B":
                            counter += 1
                        if matrix[i - 1][j - 1] == "B":
                            counter += 1
                        matrix[i][j] = counter
                    #Middle item in row conditions
                    else:
                        if matrix[i][j] == "B":
                            continue
                        if matrix[i][j - 1] == "B":
                            counter += 1
                        if matrix[i][j + 1] == "B":
                            counter += 1
                        if matrix[i - 1][j] == "B":
                            counter += 1
                        if matrix[i - 1][j - 1] == "B":
                            counter += 1
                        if matrix[i - 1][j + 1] == "B":
                            counter += 1
                        matrix[i][j] = counter
            #Middle rows conditions
            else:
                for j in range(0, len(matrix[i])):
                    counter = 0
                    #Firts item in row conditons
                    if j == 0:
                        if matrix[i][j] == "B":
                            continue
                        if matrix[i][j + 1] == "B":
                            counter += 1
                        if matrix[i - 1][j] == "B":
                            counter += 1
                        if matrix[i - 1][j + 1] == "B":
                            counter += 1
                        if matrix[i + 1][j] == "B":
                            counter += 1
                        if matrix[i + 1][j + 1] == "B":
                            counter += 1
                        matrix[i][j] = counter
                    #Last item in row conditions
                    elif j == len(matrix[i]) - 1:
                        if matrix[i][j] == "B":
                            continue
                        if matrix[i][j - 1] == "B":
                            counter += 1
                        if matrix[i - 1][j] == "B":
                            counter += 1
                        if matrix[i - 1][j - 1] == "B":
                            counter += 1
                        if matrix[i + 1][j] == "B":
                            counter += 1
                        if matrix[i + 1][j - 1] == "B":
                            counter += 1
                        matrix[i][j] = counter
                    #Middle item in row conditions
                    else:
                        if matrix[i][j] == "B":
                            continue
                        if matrix[i][j - 1] == "B":
                            counter += 1
                        if matrix[i][j + 1] == "B":
                            counter += 1
                        if matrix[i - 1][j] == "B":
                            counter += 1
                        if matrix[i - 1][j - 1] == "B":
                            counter += 1
                        if matrix[i - 1][j + 1] == "B":
                            counter += 1
                        if matrix[i + 1][j] == "B":
                            counter += 1
                        if matrix[i + 1][j - 1] == "B":
                            counter += 1
                        if matrix[i + 1][j + 1] == "B":
                            counter += 1
                        matrix[i][j] = counter
        for row in matrix:
            print(''.join(map(str, row)))

    
    def display_board(self):
        matrix = [["░" for i in range(0, self.width)] for i in range(0, self.height)]
        for row in matrix:
            print(''.join(map(str, row)))


board_one = Board()

board_one.display_board()

board_one.hidden_board()
