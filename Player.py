from Utilities import *
from Sound import *
from Stats import *
from Expl import *

playerList = []
ammoList = []


class Player:
    def __init__(self):
        self.charging = False
        self.health = 10
        self.name = "PLAYER"
        self.x = screenSize[0] / 2
        self.y = screenSize[1] - 60
        self.w = 41
        self.h = 44
        self.dmg_inflicted = 0
        self.hp = 100

        self.fire_delay_cur = 0
        self.fire_delay_max = 20


        image = pygame.image.load("./images/ships/fighter_PRIME.png").convert_alpha()

        self.image = image

        self.right = False
        self.up = False
        self.down = False
        self.left = False

        self.attack = False

        self.recentwave = 0
        self.wave = 1
        self.isboss = False

        playerList.append(self)

    def update(self):

        detectCollision(enemyList[0], self)

        if self.hp == 0:
            stats[0].game_on = False

        for x in range(0, len(enemyList)):

            if detectCollision(self, enemyList[x]):
                if enemyList[x].health > 0:
                    #print("uh-oh")
                    self.dmg_inflicted += 1
                    self.hp -= 10
                    enemyList[x].health -= 10
                    Sound.crash()
                    generateExpl(self.x - 16, self.y)

        if playerList[0].dmg_inflicted % 100 == 0 and playerList[0].dmg_inflicted != 0 and not self.isboss:
            self.wave += 1
            boss = Boss("BOSS_A")
            self.isboss = True
        
        if playerList[0].dmg_inflicted % 100 == 10 and playerList[0].dmg_inflicted != 10:
            self.isboss = False

        if playerList[0].dmg_inflicted / 10 == self.wave:

            if self.recentwave != self.wave:
                enemyList.clear()

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

            self.recentwave += 1
            self.wave += 1

        if stats[0].game_on:

            if self.right:
                if self.x < screenSize[0] - self.w:
                    self.x += 2
            if self.up:
                if self.y > 0:
                    self.y -= 2
            if self.down:
                if self.y < screenSize[1] - self.h:
                    self.y += 2
            if self.left:
                if self.x > 0:
                    self.x -= 2

            if self.attack:
                if self.fire_delay_cur == 0:
                    generateLaserAmmo()
                    self.fire_delay_cur += 1
                    if self.charging:
                        Sound.shoot()

                elif self.fire_delay_cur < self.fire_delay_max:
                    self.fire_delay_cur += 1

                else:

                    self.fire_delay_cur = 0


    def draw(self):
        if stats[0].game_on:
            screen.blit(self.image, (self.x, self.y))


class LaserAmmoLeft:
    def __init__(self):

        self.name = "LASER_BEAM"
        self.x = playerList[0].x
        self.y = playerList[0].y
        self.w = 8
        self.h = 16

        self.active = True

        # fade(pygame.image.load("./images/laser.png").convert_alpha(), self.x, self.y)
        image = pygame.image.load("./images/laser.png").convert_alpha()
        image = pygame.transform.scale(image, (self.w, self.h))

        self.image = image

        self.dashSPEED = 4

        ammoList.append(self)

    def update(self):
        if self.active:
            for x in range(0, len(enemyList)):
                if enemyList[x].health > 0:
                    if detectCollision(self, enemyList[x]):
                        # print("enemy was hit")
                        Sound.hit()
                        playerList[0].dmg_inflicted += 1
                        enemyList[x].health -= 10
                        self.active = False
                        generateExpl(self.x - 16, self.y)

            self.y -= self.dashSPEED

    def draw(self):
        if self.active:
            screen.blit(self.image, (self.x, self.y))


class LaserAmmoRight:
    def __init__(self):
        self.name = "LASER_BEAM"
        self.x = playerList[0].x + (playerList[0].w - 10)
        self.y = playerList[0].y
        self.w = 8
        self.h = 16

        self.active = True


        image = pygame.image.load("./images/laser.png").convert_alpha()
        image = pygame.transform.scale(image, (self.w, self.h))

        self.image = image

        self.dashSPEED = 4

        ammoList.append(self)

    def update(self):
        if self.active:
            for x in range(0, len(enemyList)):

                if detectCollision(self, enemyList[x]):
                    if enemyList[x].health > 0:
                        # print("enemy was hit")
                        playerList[0].dmg_inflicted += 1
                        Sound.hit()
                        enemyList[x].health -= 10
                        self.active = False
                        generateExpl(self.x - 16, self.y)

            self.y -= self.dashSPEED

    def draw(self):
        if self.active:
            screen.blit(self.image, (self.x, self.y))


def generateLaserAmmo():
    if len(ammoList) > 20:
        ammoList.pop(0)
        ammoList.pop(0)


    laserAmmo0X = LaserAmmoLeft()
    laserAmmo1X = LaserAmmoRight()

player0x = Player()
