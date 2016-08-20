import pygame
from pygame.locals import *

class ParallaxSample(object):
    def __init__(self, pygame, screen, layer_1, layer_1_r, layer_2, layer_3, xn,yn, screen_limit):
        self.screen = screen
        self.pygame = pygame
        self.clock = self.pygame.time.Clock()
        self.layer_1 = layer_1
        self.layer_1_r = layer_1_r
        self.layer_2 = layer_2
        self.layer_3 = layer_3
        self.x = xn
        self.x_1r = - (screen_limit)+20
        self.y = yn
        self.screen_limit = screen_limit
        self.orientation = 1
        self.font = self.pygame.font.SysFont("arial", 26)
        self.text = None

    def animate(self):
        self.clock.tick(120)
        self.x += self.orientation
        self.x_1r += self.orientation
        #if self.x + self.layer_1.get_width() >= self.screen_limit or self.x <= 0:
        #    self.orientation *= -1

        if self.x >= self.screen_limit:
            self.x = -self.layer_1.get_width()
        if self.x + self.layer_1.get_width() >= self.screen_limit:
            self.x_1r = -self.layer_1.get_width()

    def refresh(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.layer_1, (self.x, self.y))
        self.screen.blit(self.layer_1_r, (self.x_1r, self.y))
        self.pygame.display.update()

    def show_text(self, message):
        self.text = self.font.render(message, True, (34, 139, 34))

        self.screen.blit(self.text, (100, 25))
        self.pygame.display.update()
