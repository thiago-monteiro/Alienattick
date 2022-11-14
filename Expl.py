import pygame
import random
from GuiPrime import *

expl_list = []


class Expl:

    def __init__(self, name, x, y, w, h, strip_w, strip_h):

        self.name = name
        self.x = x
        self.y = y

        self.w = w
        self.h = h

        self.strip_w = strip_w
        self.strip_h = strip_h

        self.frame_cur = 1
        self.frame_max = self.strip_w / self.w

        self.image = pygame.image.load("./images/spritesheets/explosion.png").convert_alpha()

        self.sub = self.image.subsurface((0, 0, 32, 32))

        self.active = True

        expl_list.append(self)

    def update(self):

        if self.active:
            if self.frame_cur < self.frame_max:
                self.sub = self.image.subsurface((self.frame_cur * 32, 0, 32, 32))

                self.frame_cur += 1

            else:
                self.active = False

    def draw(self):
        if self.active:
            screen.blit(self.sub, (self.x, self.y))

def generateExpl(x, y):
    Expl("RED", x, y, 32, 32, 288, 32)
