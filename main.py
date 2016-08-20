import pygame
from pygame.locals import *
from sys import exit
from EventHandler import EventHandler

SCREEN_SIZE = (800,600)

def draw():
    screen.blit(text, (0,0))

#MAIN VOID
pygame.init()
#Habilita repetição continua de eventos KEYDOWN permitindo o KEY HOLDING HANDLING
pygame.key.set_repeat(1,1)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Background Sample")

font = pygame.font.SysFont("arial", 26)
text = font.render("Naga Siren", True, (255,0,0))

pad = pygame.image.load("img\\pad.jpg").convert_alpha()
speed = 3
player_position = {'x': 250, 'y':500}
while True:
    draw()
    event_handler = EventHandler(pygame, screen, pad, player_position,speed)
    player_position = event_handler.get_new_position()
    #x, y = event_handler(x, y, move_x, move_y)
