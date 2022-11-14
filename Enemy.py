import random
from GuiPrime import *
from Colors import *

enemyList = []

class enemyStatic:
    def __init__(self, name):
        self.name = name
        self.alive = True

        self.dashRIGHT = False
        self.dashLEFT = False

        self.right = False
        self.up = False
        self.down = False
        self.left = False

        self.bank_max = 30
        self.bank_cur = 0

        self.image = None

        self.attack = False

        self.init_config()

        enemyList.append(self)
    
    def init_config(self):
        pass

    def draw(self):
        if self.health > 0:
            screen.blit(self.image, (self.x, self.y))

class Enemy(enemyStatic):    
    def init_config(self):
        self.x = random.randint(-5, screenSize[0])
        self.y = 0
        self.w = 40
        self.h = 33
        self.health = 10

        image = pygame.image.load("./images/ships/enemy.png").convert_alpha()

        self.image = image

    def update(self):

        if self.x < screenSize[0] - self.w:
            self.x += 2

        if self.x > 0:
            self.x -= 2

        if self.alive == True:
            #self.x += random.randint(-5, 5)

            self.y+=1

            if self.y < screenSize[1]:
                self.y +=1

            else:
                self.y = -55

            if self.attack:
                print(self.name + "enemy is attacking...")
            if self.up:
                self.y -= 2
            if self.down:
                self.y += 2

            if self.dashLEFT:
                self.x -= 1

            if self.dashRIGHT:
                self.x += 1

            if self.bank_cur > self.bank_max:
                if self.dashRIGHT:
                    self.dashLEFT = True
                    self.dashRIGHT = False
                else:
                    self.dashRIGHT = True
                    self.dashLEFT = False

                self.bank_cur = 0
            else:
                self.bank_cur +=1

            if self.attack:
                self.attack = False


class SpeedSkater(enemyStatic):
    def init_config(self):
        self.x = random.randint(-5, screenSize[0])
        self.y = 0
        self.w = 32
        self.h = 32
        self.health = 10
        self.hp_max = 10

        image = pygame.image.load("./images/ships/speedskater.png").convert_alpha()

        self.image = image

    def update(self):

        if self.x < screenSize[0] - self.w:
            self.x += 2

        if self.x > 0:
            self.x -= 2

        if self.alive == True:
            self.x += random.randint(-5, 5)

            self.y+=1

            if self.y < screenSize[1]:
                self.y += 10

            else:
                self.y = -55

            if self.attack:
                print(self.name + "enemy is attacking...")

            if self.up:
                self.y -= 2
            if self.down:
                self.y += 2

            if self.dashLEFT:
                self.x -= 1

            if self.dashRIGHT:
                self.x += 1

            if self.bank_cur > self.bank_max:
                if self.dashRIGHT:
                    self.dashLEFT = True
                    self.dashRIGHT = False
                else:
                    self.dashRIGHT = True
                    self.dashLEFT = False

                self.bank_cur = 0
            else:
                self.bank_cur +=1

            if self.attack:
                self.attack = False


class JitterBug(enemyStatic):
    def init_config(self):
        self.x = random.randint(-5, screenSize[0])
        self.y = 0
        self.w = 32
        self.h = 32
        self.health = 10
        self.hp_max = 10

        image = pygame.image.load("./images/ships/jitterbug.png").convert_alpha()

        self.image = image

    def update(self):

        if self.x < screenSize[0] - self.w:
            self.x += 20

        if self.x > 0:
            self.x -= 20

        if self.alive == True:
            self.x += random.randint(-50, 50)

            self.y+=1

            if self.y < screenSize[1]:
                self.y += 1

            else:
                self.y = -55

            if self.attack:
                print(self.name + "enemy is attacking...")

            if self.up:
                self.y -= 2
            if self.down:
                self.y += 2

            if self.dashLEFT:
                self.x -= 1

            if self.dashRIGHT:
                self.x += 1

            if self.attack:
                self.attack = False


class Boss(enemyStatic):
    def init_config(self):
        self.x = random.randint(-5, screenSize[0])
        self.y = 352
        self.w = 151
        self.h = 200
        self.health = 100
        self.hp_max = 100

        image = pygame.image.load("./images/ships/bossFighter.png").convert_alpha()

        self.image = image

    def update(self):

        if self.x < screenSize[0] - self.w:
            self.x += 20

        if self.x > 0:
            self.x -= 20

        if self.alive == True:
            self.x += random.randint(-20, 20)

            self.y+=1

            if self.y < screenSize[1]:
                self.y += 3

            else:
                self.y = -55

            if self.attack:
                print(self.name + "enemy is attacking...")

            if self.up:
                self.y -= 2
            if self.down:
                self.y += 2

            if self.dashLEFT:
                self.x -= 1

            if self.dashRIGHT:
                self.x += 1

            if self.bank_cur > self.bank_max:
                if self.dashRIGHT:
                    self.dashLEFT = True
                    self.dashRIGHT = False
                else:
                    self.dashRIGHT = True
                    self.dashLEFT = False

                self.bank_cur = 0
            else:
                self.bank_cur +=1

            if self.attack:
                self.attack = False

    def draw(self):
        if self.health > 0:
            screen.blit(self.image, (self.x, self.y))

            pygame.draw.rect(screen, RED,   [self.x - 20, self.y - 40, self.hp_max, 10])
            pygame.draw.rect(screen, GREEN, [self.x - 20, self.y - 40, self.health, 10])



enemy0X = SpeedSkater("DRONE_A")
enemy1X = SpeedSkater("DRONE_A")
enemy2X = JitterBug("DRONE_A")
enemy3X = JitterBug("DRONE_A")
enemy4X = JitterBug("DRONE_A")
enemy5X = Enemy("DRONE_A")
enemy6X = Enemy("DRONE_A")
enemy7X = Enemy("DRONE_A")
enemy8X = Enemy("DRONE_A")
enemy9X = Enemy("DRONE_A")
