from Enemy import *

pygame.font.init()

stats = []

class Stats:

    def __init__(self):
        self.wave = 1

        self.enemy_dead = 0

        self.game_on = True

        self.debug = True

        self.stage = 1

        self.font = pygame.font.Font(None, 60)

        stats.append(self)

    def draw(self):

        if not self.game_on:
            label = self.font.render("gAMe OVer", True, pygame.Color("white"))
            screen.blit(label, (250, 250))


Stats()
