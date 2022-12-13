import pygame

from setting import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = (
                        pygame.image.load("images/scratr.png"), 
                        pygame.image.load("images/scratl.png")
        )

        self.image = self.images[0]

        self.image = pygame.image.load("images/scratr.png")

        self.rect = self.image.get_rect()
        self.radius = 83
        #pygame.draw.circle(self.image, BLUE, self.rect.center, self.radius)
               
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT - 70
        
        self.playing = True
        self.mask = pygame.mask.from_surface(self.image)

    def collide_with(self, sprites):
        objects = pygame.sprite.spritecollide(self, sprites, False, pygame.sprite.collide_mask)
        if objects:
            return objects[0]

    def draw(self, image):
        self.move()
    
    def move(self):
        self.validate_move()

    def mov_left(self):
        if self.playing:
            self.validate_move()
            self.rect.x -= 3

            self.image = self.images[1]
        

    def mov_right(self):
        if self.playing:
            self.validate_move()
            self.rect.x += 3

            self.image = self.images[0]
        
          
    def validate_move(self):
        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > (WIDTH - WIDTH_PLAYER):
            self.rect.x = WIDTH - WIDTH_PLAYER 


    def stop(self):
        self.playing = False


   
    
    
    
        
        