import pygame
pygame.init()

from utils import *
from vars import *

class base():
    def __init__(self, x, y, surface, white):
        self.win = surface
        if white:
            self.white = True
        else:
            self.white = False
        self.rect = pygame.Rect(x, y, square_size, square_size)
        self.dragx, self.dragy  = x, y
        self.selected = False
        self.move = False
        self.turn = False
        self.image()

    def image(self):
        pass
    def restrict(self, x, y, pieces_list):
        pass
    def rules(self,x,y, pieces_list):
        pass   
    def highlight(self):
        if self.selected:
            pygame.draw.rect(self.win, (0, 255, 0), (self.dragx, self.dragy, square_size, square_size))

    def draw(self):
        self.win.blit(self.img, self.rect)

    def click(self, pieces_list):
        if pygame.mouse.get_pressed()[0] and pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos()) and not self.selected and not self.move:
            self.selected = True
            self.dragx, self.dragy = self.rect.x, self.rect.y

        if self.selected and not self.move:
            if pygame.mouse.get_pressed()[0] and not (pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos())):
                mousex, mousey = get_coords(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                if self.rules(mousex, mousey, pieces_list) and self.restrict(mousex, mousey, pieces_list):
                    self.rect.x, self.rect.y = mousex, mousey
                    self.move = True
                    self.turn = True

        if self.move and self.selected:
            if not pygame.mouse.get_pressed()[0]:# and not pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos()):
                self.move = False
                self.selected = False

        if pygame.mouse.get_pressed()[0]:
            if self.selected and not self.move and not (pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos())):
                self.selected = False

class rook(base):
    def image(self):
        if self.white:
            self.img = pygame.transform.scale(pygame.image.load("images/w-rook.png"), (square_size, square_size))
        else:
            self.img = pygame.transform.scale(pygame.image.load("images/b-rook.png"), (square_size, square_size))
            self.white = False

    def restrict(self, x, y, pieces_list):
        for piece in pieces_list:
            if piece != None:
                if x == piece.rect.x:
                    if self.rect.y > piece.rect.y:
                        if y<piece.rect.y:
                            return False
                    elif self.rect.y < piece.rect.y:
                        if y>piece.rect.y:
                            return False
                elif y == piece.rect.y:
                    if self.rect.x > piece.rect.x:
                        if x<piece.rect.x:
                            return False
                    elif self.rect.x < piece.rect.x:
                        if x>piece.rect.x:
                            return False
                '''if y == piece.rect.y:
                    if self.rect.x > piece.rect.x:
                        if x<=piece.rect.x:
                            return False
                    elif self.rect.x < piece.rect.x:
                        if x>=piece.rect.x:
                            return False
                elif x == piece.rect.x:
                    if self.rect.y > piece.rect.y:
                        if y<=piece.rect.y:
                            return False
                    elif self.rect.y < piece.rect.y:
                        if y>=piece.rect.y:
                            return False'''
        return True

    def rules(self,x,y, pieces_list):
        if (((x==self.rect.x) or (y==self.rect.y)) and not((x==self.rect.x) and (y==self.rect.y))):
                for i in pieces_list:
                    if i != None:
                        if (i.rect.x == x) and (i.rect.y == y):
                            if i.white == self.white:
                                return False 
                return True
        return False

class bishop(base):
    def image(self):
        if self.white:
            self.img = pygame.transform.scale(pygame.image.load("images/w-bishop.png"), (square_size, square_size))
        else:
            self.img = pygame.transform.scale(pygame.image.load("images/b-bishop.png"), (square_size, square_size))
            self.white = False

    def restrict(self, x, y, pieces_list):
        for piece in pieces_list:
            if piece != None:
                return True

    def rules(self,x,y, pieces_list):
        if (self.rect.x - x)**2 == (self.rect.y - y)**2:
                for i in pieces_list:
                    if i != None:
                        if (i.rect.x == x) and (i.rect.y == y):
                            if i.white == self.white:
                                return False 
                return True
        return False