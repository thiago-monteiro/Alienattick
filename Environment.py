from Config import *
from Player import *
from GuiPrime import *


dirtList = []
envList = []


class Star:
    def __init__(self):

        self.type = random.randint(0, 1)

        self.x = random.randint(-5, screenSize[0])
        self.y = random.randint(-5, screenSize[1])
        self.option = random.randint(0, 1)
        if self.y > screenSize[1] - 100:
            if self.option == 0:
                self.x = random.randint(-5, (screenSize[0] / 2) - 41)
            else:
                self.x = random.randint((screenSize[0] / 2) + 41, screenSize[0])

        if self.type == 0:
            image = pygame.image.load("./images/star.png")

        if self.type == 1:
            image = pygame.image.load("./images/star01.png")


        self.image = image

        self.is_offscreen = False

        envList.append(self)

    def update(self):

        if self.y < screenSize[1]:
            self.y += optionList[0].star_speed
            # self.y  = playerList[0].y + 17

        else:
            self.x = random.randint(-5, screenSize[0])

    def draw(self):

        screen.blit(self.image, (self.x, self.y))


class Rocks:
    def __init__(self):
        self.x = random.randint(-5, screenSize[0])
        self.y = random.randint(-5, screenSize[1])
        self.option = random.randint(0, 1)
        if self.y > screenSize[1] - 100:
            if self.option == 0:
                self.x = random.randint(-5, (screenSize[0] / 2) - 41)
            else:
                self.x = random.randint((screenSize[0] / 2) + 41, screenSize[0])

        image = pygame.image.load("./images/rocks.png")

        image = pygame.transform.scale(image, (16, 16))

        self.image = image

        dirtList.append(self)

    def update(self):

        self.y += 1

        if self.y < screenSize[1]:
            self.y += optionList[0].world_speed

        else:
            self.y = world_speed

    def draw(self):

        screen.blit(self.image, (self.x, self.y))


for x in range(0, 7):
    star0x = Star()

for x in range(0, 30):
    rock0x = Rocks()
    for x in range(len(dirtList)):
        for y in range(len(dirtList)):
            if x != y and abs(dirtList[x].y - dirtList[y].y) < 16 or x != y and abs(dirtList[x].x - dirtList[y].x) < 16:
                if random.randint(0, 1) == 1:
                    dirtList[y].y = dirtList[x].y + 16
                else:
                    dirtList[y].x = dirtList[x].x + 16
