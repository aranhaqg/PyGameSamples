import pygame
from pygame.locals import *

class EventHandler(object):
    def __init__(self, pygame, screen, image, position, speed):
        self.screen = screen
        self.pygame = pygame
        self.image = image
        self.position = position
        self.speed = speed
        #self.position = {'x' : 250, 'y' : 500}
        self.move_x=0
        self.move_y=0

    def get_new_position(self):
        for event in self.pygame.event.get():
            if event.type == QUIT:
                self.pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.move_x = -1*self.speed
                elif event.key == K_RIGHT:
                    self.move_x = 1*self.speed
                elif event.key == K_UP:
                    self.move_y = -1*self.speed
                elif event.key == K_DOWN:
                    self.move_y = 1*self.speed

            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    self.move_x = 0
                elif event.key == K_RIGHT:
                    self.move_x = 0
                elif event.key == K_UP:
                    self.move_y = 0
                elif event.key == K_DOWN:
                    self.move_y = 0

            self.position['x'] += self.move_x
            self.position['y'] += self.move_y

            # Limit x boundaries
            if (self.position['x'] < -50):
                self.position['x'] = -50
            elif (self.position['x'] > 525):
                self.position['x'] = 525
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.image, (self.position['x'], self.position['y']))
            self.pygame.display.update()
        return self.position