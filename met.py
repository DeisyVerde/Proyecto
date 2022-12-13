import pygame
import random

from setting import HEIGHT
from setting import WIDTH
from setting import BLUE

class Meteorite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/meteorito.png")

        self.rect = self.image.get_rect()
        self.radius = 47
        #pygame.draw.circle(self.image, BLUE, self.rect.center, self.radius)


        self.rect.x = random.randrange(WIDTH- self.rect.width)
        self.rect.y = - self.rect.width
        self.mask = pygame.mask.from_surface(self.image)

        self.vel_y = random.randrange(2, 3)
        self.vel_x = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH- self.rect.width)
            self.rect.y = - self.rect.width

            self.vel_y = random.randrange(3, 5)
            self.vel_x = random.randrange(-3, 3)
        
    def stop(self):
        self.vel_y = 0