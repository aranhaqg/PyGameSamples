import pygame
from pygame.locals import *
from sys import exit
from ParallaxSample import ParallaxSample

SCREEN_SIZE = (600, 450)

def atualizar():
    clock.tick(120)
    global xn, sentido
    xn = xn + 1 * sentido
    if (xn >= 450 or xn <= 0):
        sentido *= -1

def desenhar():
    screen.fill((255, 255, 255))
    screen.blit(imagem, (xn, yn))
    screen.blit(texto, (100, 25))
    pygame.display.update()

pygame.init()

pygame.key.set_repeat(1, 1)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Kirby UFO")



layer_1 = pygame.image.load("img\\naga_siren.png").convert_alpha()
layer_1_r = pygame.image.load("img\\naga_siren2.png").convert_alpha()
layer_2 = pygame.image.load("img\\pad.jpg").convert_alpha()
layer_3 = pygame.image.load("img\\pad.jpg").convert_alpha()

xn, yn = (0, 0)
xn_limit = 600
#yn_limit = screen.get_size()

parallax = ParallaxSample( pygame, screen, layer_1, layer_1_r, layer_2, layer_3, xn,yn, xn_limit)

while True:
    parallax.animate()
    parallax.refresh()
    #parallax.show_text("AHOY!")