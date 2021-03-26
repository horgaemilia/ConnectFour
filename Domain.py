import numpy as np



class Table:
    def __init__(self):
        list1 = []
        for i in range(42):
            list1.append(0)
        list1 = np.array(list1)
        shape = (6,7)
        matrix = list1.reshape(shape)
        self.__table = matrix

    def get_element(self, i, j):
        return self.__table[i][j]

    def get_row(self,col): # returns the row corresponding to the column to find where the piece lands
        row = None
        for i in range(6):
            if self.__table[i][col] == 0:
                row = i
        if row==None:
            return None
        else:
            return row

    def check_win(self,row,col,check):  # i checked all the winning cases, all of them to find a string of 4 same pieces
        if row <= 2:
            if self.__table[row + 1][col] == self.__table[row + 2][col] and self.__table[row + 1][col] == \
                    self.__table[row + 3][col] and self.__table[row + 1][col] == check:
                return 1
        if 0 <= col <= 3:
            if self.__table[row][col + 1] == self.__table[row][col + 2] and self.__table[row][col + 1] == \
                    self.__table[row][col + 3] and self.__table[row][col + 1] == check:
                return 1
        if 1 <= col <= 4:
            if self.__table[row][col - 1] == self.__table[row][col + 1] and self.__table[row][col - 1] == \
                    self.__table[row][col + 2] and self.__table[row][col - 1] == check:
                return 1
        if 2 <= col <= 5:
            if self.__table[row][col - 2] == self.__table[row][col - 1] and self.__table[row][col - 2] == \
                    self.__table[row][col + 1] and self.__table[row][col - 2] == check:
                return 1
        if 3 <= col <= 6:
            if self.__table[row][col - 3] == self.__table[row][col - 2] and self.__table[row][col - 3] == \
                    self.__table[row][col - 1] and self.__table[row][col - 3] == check:
                return 1
        if 0 <= row <= 2 and 0 <= col <= 3:
            if self.__table[row + 1][col + 1] == self.__table[row + 2][col + 2] and self.__table[row + 1][col + 1] == \
                    self.__table[row + 3][col + 3] and self.__table[row + 1][col + 1] == check:
                return 1
        if 1 <= row <= 3 and 1 <= col <= 4:
            if self.__table[row - 1][col - 1] == self.__table[row + 1][col + 1] and self.__table[row - 1][col - 1] == \
                    self.__table[row + 2][col + 2] and self.__table[row - 1][col - 1] == check:
                return 1
        if 2 <= row <= 4 and 2 <= col <= 5:
            if self.__table[row - 2][col - 2] == self.__table[row - 1][col - 1] and self.__table[row - 2][col - 2] == \
                    self.__table[row + 1][col + 1] and self.__table[row - 2][col - 2] == check:
                return 1
        if 3 <= row <= 5 and 3 <= col <= 6:
            if self.__table[row - 3][col - 3] == self.__table[row - 2][col - 2] and self.__table[row - 3][col - 3] == \
                    self.__table[row - 1][col - 1] and self.__table[row - 3][col - 3] == check:
                return 1
        if 3 <= row <= 5 and 0 <= col <= 3:
            if self.__table[row - 1][col + 1] == self.__table[row - 2][col + 2] and self.__table[row - 1][col + 1] == \
                    self.__table[row - 3][col + 3] and self.__table[row - 1][col + 1] == check:
                return 1
        if 2 <= row <= 4 and 1 <= col <= 4:
            if self.__table[row + 1][col - 1] == self.__table[row - 1][col + 1] and self.__table[row + 1][col - 1] == \
                    self.__table[row - 2][col + 2] and self.__table[row + 1][col - 1] == check:
                return 1
        if 1 <= row <= 3 and 2 <= col <= 5:
            if self.__table[row + 2][col - 2] == self.__table[row + 1][col - 1] and self.__table[row + 2][col - 2] == \
                    self.__table[row - 1][col + 1] and self.__table[row + 2][col - 2] == check:
                return 1
        if 0 <= row <= 2 and 3 <= col <= 6:
            if self.__table[row + 3][col - 3] == self.__table[row + 2][col - 2] and self.__table[row + 3][col - 3] == \
                    self.__table[row + 1][col - 1] and self.__table[row + 3][col - 3] == check:
                return 1
        return 0

    def move_hooman(self, i, j):  # puts 1 for the player
        self.__table[i][j] = 1

    def move_computer(self, i, j): # puts 2 for the computer
        self.__table[i][j] = 2

    def get_table(self): # returs the table
        return self.__table




'''
    def print_t(self):
        for j in range(6):
            msg = ""
            for i in range(7):
                msg +=str(self.__table[j][i]) + " "
            print(msg)
'''

