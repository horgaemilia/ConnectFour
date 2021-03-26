import pygame
import sys
from Domain import *
from Service import *


class Gui:
    def __init__(self, serv):
        self.__service = serv
        pygame.init()
        self._square = 100
        self._row = 6
        self._col = 7
        self._width = self._col * self._square
        self._height = (self._row + 1) * self._square
        self._size = (self._width, self._height)
        self._screen = pygame.display.set_mode(self._size)
        self._myfont = pygame.font.SysFont("monospace",60)

    def print_board(self):
        for c in range(self._col):
            for r in range(self._row):
                pygame.draw.rect(self._screen, (0, 0, 255),
                                 (c * self._square, (r + 1) * self._square, self._square, self._square))
                if self.__service.get_element(r, c) == 0:
                    pygame.draw.circle(self._screen, (0, 0, 0), (
                    c * self._square + self._square // 2, (r + 1) * self._square + self._square // 2),
                                       self._square // 2 - 5)
                if self.__service.get_element(r, c) == 1:
                    pygame.draw.circle(self._screen, (255, 0, 0), (
                        c * self._square + self._square // 2, (r + 1) * self._square + self._square // 2),
                                       self._square // 2 - 5)
                if self.__service.get_element(r,c) == 2:
                    pygame.draw.circle(self._screen, (255, 255, 0), (
                    c * self._square + self._square // 2, (r + 1) * self._square + self._square // 2),
                                       self._square // 2 - 5)

        pygame.display.update()

    def gui_make_a_move(self, j):
        self.__service.make_a_move_hooman(int(j))

    def start_game(self):
        running = True
        while running:
            self.print_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self._screen,(0,0,0),(0,0,self._width,self._square))
                    posx = event.pos[0]
                    pygame.draw.circle(self._screen, (255, 0, 0), (posx,self._square//2),self._square // 2 - 5)
                    pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    col = posx // self._square
                    if self.__service.game_winner(col,"user"):
                        self.gui_make_a_move(col)
                        self.print_board()
                        pygame.draw.rect(self._screen, (0, 0, 0), (0, 0, self._width, self._square))
                        pygame.display.update()
                        label = self._myfont.render("Player has won",1,(255,0,0))
                        self._screen.blit(label,(40,10))
                        pygame.display.update()
                        running = False
                    else:
                        self.gui_make_a_move(col)
                        self.print_board()
                        col, row = self.__service.computer_move_col()
                        if self.__service.game_winner(col, "computer"):
                            self.__service.computer_move(row, col)
                            self.print_board()
                            pygame.draw.rect(self._screen, (0, 0, 0), (0, 0, self._width, self._square))
                            pygame.display.update()
                            text = self._myfont.render("Computer has won", 2, (255, 255, 0))
                            self._screen.blit(text, (40, 10))
                            pygame.display.update()
                            running = False
                        else:
                            self.__service.computer_move(row, col)
                            self.print_board()
                if running == False:
                        pygame.time.wait(4000)

t = Table()
s = Service(t)
g = Gui(s)
g.start_game()
