import pygame
pygame.mixer.init()


class Sound:

    def startup():
        pygame.mixer.stop()
        pygame.mixer.music.load('./sound/engine.wav')
        pygame.mixer.music.play(0)

    def hit():
        pygame.mixer.stop()
        pygame.mixer.music.load('./sound/hit_hurt.wav')
        pygame.mixer.music.play(0)

    def shoot():
        pygame.mixer.stop()
        pygame.mixer.music.load('./sound/laser_shoot.wav')
        pygame.mixer.music.play(0)

    def crash():
        pygame.mixer.stop()
        pygame.mixer.music.load('./sound/crash.wav')
        pygame.mixer.music.play(0)

    def stop():
        pygame.mixer.music.stop()