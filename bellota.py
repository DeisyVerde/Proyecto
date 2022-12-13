import pygame
import random
from setting import HEIGHT, WIDTH, WHITE

class Bellota(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/bellota.png")

        self.rect = self.image.get_rect()
        self.radius = 20
        #pygame.draw.circle(self.image, WHITE, self.rect.center, self.radius)


        
        self.rect.x = random.randrange(WIDTH- self.rect.width)
        self.rect.y = - self.rect.width

        self.vel_y = random.randrange(2, 3)
        
    def update(self):
        self.rect.top += self.vel_y

        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH- self.rect.width)
            self.rect.y = - self.rect.width

            self.vel_y = random.randrange(3, 5)

    def stop(self):
        self.vel_y = 0
        
    