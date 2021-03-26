from Domain import*
from random import randint

class Service:
    def __init__(self,table):
        self.__table = table

    def get_table(self): #returns the table from the domain
        return self.__table.get_table()
    def check_col(self,col):
        return self.__table.get_row(col)
    def make_a_move_hooman(self,j): #it makes the human move
        c = 0
        row = self.__table.get_row(j)
        if row!=None:
            self.__table.move_hooman(row,j)
            c = 1
        if c == 0:
            raise ValueError("row is full")

    def make_a_move_user(self,j):
        c = 0
        row = self.__table.get_row(j)
        if row != None:
            self.__table.move_computer(row, j)
            c = 1
        if c == 0:
            raise ValueError("row is full")

    def computer_move_col(self): # it checks to see if the player has 3 pieces and blocks them if not he searches for the computer to have 3 pieces and it puts the next one
        for i in range(7):       #if not it will put a piece random
            row = self.__table.get_row(i)
            if row != None:
                if self.game_winner(i,"computer") == 1:
                    row = self.__table.get_row(i)
                    print("you loser. I win")
                    return i,row
        for i in range(7):
            row = self.__table.get_row(i)
            if row!= None:
                if self.game_winner(i,"user") == 1:
                    row = self.__table.get_row(i)
                    return i,row
        while True:
            col = randint(0,6)
            row = self.__table.get_row(col)
            if row!=None:
                return col,row

    def computer_move(self,row,col):  # calls the function from above
        self.__table.move_computer(row,col)

    def game_winner(self,col,user): # searches for the game winner and returns 1 or 0 which he gets from the check_win function
        if user == "user":
            check = 1
        else:
            check = 2
        row = self.__table.get_row(col)
        if row==None:
            row=0
        ended = self.__table.check_win(row,col,check)
        return ended

    def get_element(self,i,j):
        return self.__table.get_element(i,j)







