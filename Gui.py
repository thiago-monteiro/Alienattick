from Player import *
from Colors import *

pygame.font.init()

gui_item_list = []


class GuiItem:

    def __init__(self, name, x, y, w, h):

        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        font = pygame.font.SysFont("Monospace", 35)
        self.font = font

        if self.name == "SCORE_GUI":
            score_font = pygame.font.Font("./images/fonts/score_font.TTF", 30)
            win_banner_font = pygame.font.Font(None, 60)
            self.score_font = score_font
            self.win_banner_font = win_banner_font

        gui_item_list.append(self)

    def draw(self):

        if self.name == "TITLE":
            label = self.font.render("aLiEnATTicK", True, WHITE)
            screen.blit(label, (256, 256))

        elif self.name == "SCORE_GUI":
            counter = (pygame.time.get_ticks()) / 1000
            counter -= 6
            counter = str(round(counter))
            screen.blit(self.font.render("Time: " + counter, True, (255, 255, 255)), (620, 30))

            if stats[0].game_on:
                screen.blit(self.font.render("Health: " + str(playerList[0].hp), True, (255, 255, 255)), (620, 60))

            screen.blit(self.font.render("Wave: " + str(playerList[0].wave), True, (255, 255, 255)), (620, 90))

            pygame.draw.rect(screen, BLACK,(0,0,186,46))
            pygame.draw.rect(screen, WHITE,(6,6,174,34))
            dmg = self.score_font.render("SCORE: " + str(playerList[0].dmg_inflicted), 1, BLACK)
            screen.blit(dmg, (self.x + 15, self.y + 2))


GuiItem("TITLE", 0, 0, 0, 0)
