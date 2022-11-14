import time
import sys
from Gui import *
from Environment import *
from Enemy import *
from Sound import *
from Expl import *

font = pygame.font.SysFont("Monospace", 30)
done = False
icon = playerList[0].image
pygame.display.set_icon(icon)


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                # print("down or s key pressed")
                playerList[0].down = True

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                # print("right or d key pressed")
                playerList[0].right = True

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                # print("left or a key pressed")
                playerList[0].left = True

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                # print("up or w key pressed")
                playerList[0].up = True

            if event.key == pygame.K_SPACE:
                # print("SPACE key pressed will self destruct in three seconds")
                playerList[0].attack = True
                playerList[0].charging = True

            if event.key == pygame.K_KP_ENTER:
                optionList[0].increase_speed()

            if event.key == pygame.K_BACKSPACE:
                optionList[0].decrease_speed()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                # print("down or s key released")
                playerList[0].down = False

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                # print("right or d key released")
                playerList[0].right = False

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                # print("left or a key released")
                playerList[0].left = False

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                # print("up or w key released")
                playerList[0].up = False

            if event.key == pygame.K_SPACE:
                # print("SPACE key released will self destruct in three seconds")
                playerList[0].charging = False
                if not playerList[0].charging:
                    Sound.stop()
                playerList[0].attack = False

    for u in range(0, len(envList)):
        envList[u].update()

    for u in range(0, len(playerList)):
        playerList[u].update()

    for u in range(0, len(dirtList)):
        dirtList[u].update()

    for u in range(0, len(enemyList)):
        enemyList[u].update()

    for u in range(0, len(ammoList)):
        ammoList[u].update()

    for u in range(0, len(expl_list)):
        expl_list[u].update()


def fade_in():

    fade_in_time = 5
    fade_in_easing = lambda y: y

    clock = pygame.time.Clock()

    text_rect = icon.get_rect(center=(screenSize[0] / 2 + 16, screenSize[1] - 44))

    st_fade_in = 0
    st_fade_out = 1

    state = st_fade_in
    last_state_change = time.time()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()

        state_time = time.time() - last_state_change

        if state == st_fade_in:
            if state_time >= fade_in_time:
                state = st_fade_out
                state_time -= fade_in_time
                last_state_change = time.time() - state_time

        if state == st_fade_in:
            alpha = fade_in_easing(0.9 * state_time / fade_in_time)
            rt = icon
            surf2 = pygame.surface.Surface((text_rect.width, text_rect.height))
            surf2.set_alpha(255 * alpha)

            for u in range(0, len(gui_item_list)):
                gui_item_list[u].draw()

            for g in range(0, len(envList)):
                envList[g].draw()

            for u in range(0, len(dirtList)):
                dirtList[u].draw()

            for u in range(0, len(enemyList)):
                enemyList[u].draw()

            surf2.blit(rt, (0, 0))
            screen.blit(surf2, text_rect)

        else:
            Sound.startup()
            gui_item_list.pop(0)
            GuiItem("SCORE_GUI", 0, 0, 185, 46)
            while not done:


                if playerList[0].hp < 1:
                    stats[0].game_on = False

                update()

                screen.fill(BACKGROUND)

                for g in range(0, len(envList)):
                    envList[g].draw()

                for u in range(0, len(dirtList)):
                    dirtList[u].draw()

                for u in range(0, len(playerList)):
                    playerList[u].draw()

                for u in range(0, len(enemyList)):
                    enemyList[u].draw()

                for u in range(0, len(ammoList)):
                    ammoList[u].draw()

                for u in range(0, len(expl_list)):
                    expl_list[u].draw()

                for u in range(0, len(gui_item_list)):
                    gui_item_list[u].draw()
            

                stats[0].draw()

                clock.tick(60)

                pygame.display.flip()

        pygame.display.flip()
        clock.tick(60)


try:
    fade_in()

except pygame.error:
    pass
