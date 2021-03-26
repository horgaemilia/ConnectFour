from Domain import*
from Service import*
import re

class Ui:
    def __init__(self,service):
        self.__service = service

    def ui_make_a_move(self,j):
        self.__service.make_a_move_hooman(int(j))

    def print_table(self):
        print(self.__service.get_table())
        print('\n')
    def ask_for_col(self):
        col=int(input("enter the col you want to make move on: "))
        if col<=0 or col>7:
            raise ValueError("I kindly ask you to go again")
        if self.__service.check_col(col-1) is None:
            raise ValueError("I kindly ask you to  go again")
        return col-1

    def start(self):
        filter = input(print("Give the filter string:"))
        print(filter)
        while True:
            while True:
                try:
                    col=self.ask_for_col()
                    break
                except ValueError as exception:
                    print(exception.args[0])
            if self.__service.game_winner(col,"user"):
                if re.match(filter, "User has won") == None:
                    print("User has won")
                self.ui_make_a_move(col)
                self.print_table()
                break
            self.ui_make_a_move(col)
            self.print_table()
    # Pana aici o fost mutarea lu individ. De aici vine intelectul superior COMPUTER
            col,row=self.__service.computer_move_col()
            if self.__service.game_winner(col,"computer"):
                if re.match(filter, "Computer has won") == None:
                    print("Computer has won")
                self.__service.computer_move(row, col)
                self.print_table()
                break
            self.__service.computer_move(row,col)
            self.print_table()



t = Table()
s = Service(t)
ui = Ui(s)
ui.start()