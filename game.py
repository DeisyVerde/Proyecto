#impotar modulos necesarios para el desarrollo
import sys
import pygame
import random

from setting import *
from player import Player
from met import Meteorite
from bellota import Bellota

clock = pygame.time.Clock()

class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption(TITLE)

        self.running = True

        self.clock = pygame.time.Clock()

        self.font = pygame.font.match_font(FONT)

        try:
            self.highscore = int(self.get_highscore())
        except:
            self.highscore = 0


    def start(self):
        self.get_highscore()
        self.menu()
        self.new()
        

    def new(self):
        self.score = 0
        self.highscore = 0
        
        self.playing = True
        
        self.back = pygame.image.load("images/fondo.jpg").convert()
        self.generate_elements()
        self.run()
        


    def generate_elements(self):
        self.player = Player()
        self.bellota = Bellota()
        self.met = Meteorite()
        
        self.sprites = pygame.sprite.Group()
        self.bellotas = pygame.sprite.Group()
        self.mets = pygame.sprite.Group()

        self.sprites.add(self.player)
        
        self.generate_bellotas()
        self.generate_mets()
        

    def generate_bellotas(self):

        if not len(self.bellotas) > 0:
            for b in range(5):
                self.bellota = Bellota()

                self.sprites.add(self.bellota)
                self.bellotas.add(self.bellota)

    def generate_mets(self):

        if not len(self.mets) > 0:
            for b in range(2):
                self.met = Meteorite()

                self.sprites.add(self.met)
                self.mets.add(self.met)


    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
    

        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_LEFT]:
            self.player.mov_left()

        if key_pressed[pygame.K_RIGHT]:
            self.player.mov_right()

        if key_pressed[pygame.K_r] and not self.playing:
            self.new()

        if self.score > self.highscoretop:
                self.highscore = self.score

                with open("Heighscore.txt", "w") as f:
                    f.write(str(self.score))
        else:
            self.display_text("Highscore:" + (str(self.highscoretop)),36, BLACK, 900, 30)




    def draw(self):
        
        self.surface.blit(self.back, (0,0))
        
        self.draw_text()

        self.sprites.draw(self.surface)

        pygame.display.flip()
        

    def update(self):
        if self.playing:

            bellota = self.player.collide_with(self.bellotas)
            
            if bellota:
                self.score +=1
                bellota.kill()
                sound  = pygame.mixer.Sound("sounds/bellsound.wav")
                sound.play()

            met = self.player.collide_with(self.mets)
            if met:
                self.stop()
                sound  = pygame.mixer.Sound("sounds/metsound.wav")
                sound.play()

            
            self.sprites.update()
            self.update_elements(self.bellotas)
            self.update_elements(self.mets)
            self.generate_bellotas()
            self.generate_mets()

                
    def update_elements(self, elements):
        for element in elements:
            if not element.rect.bottom > 0:
                element.kill()
 
        
    def stop(self):
        self.player.stop()
        self.stop_elements(self.mets)

        self.playing = False

    def stop_elements(self, elements):
        for element in elements:
            element.stop()

    def score_format(self):
        return "Score : {}". format(self.score)
        
    def get_highscore(self):
        with open ("Heighscore.txt", "r") as f:
            self.highscoretop = int(f.read())


    def draw_text(self):
        self.display_text(self.score_format(),36, BLACK, 100, 30)
        self.display_text("Highscore:" + (str(self.highscoretop)),36, BLACK, 900, 30)

        if not self.playing:
            self.display_text("Game over", 50, RED, WIDTH//2, 50)
            if self.score > self.highscoretop:
                self.display_text("Lograste un nuevo Highscore!", 30, RED, WIDTH//2, 90)
                
            self.display_text("Presiona r para comenzar de nuevo ", 30, BLUE, WIDTH//2, 130)
        
            
    def display_text(self, text, size, color, pos_x, pos_y):
        #ice = pygame.font.match_font("Ice")
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)

        self.surface.blit(text, rect)

    def menu(self):
        self.menu = pygame.image.load("images/menu.png").convert()
        self.surface.blit(self.menu, (0,0))
        self.display_text("Presiona una tecla para iniciar el juego", 36, WHITE, WIDTH// 2, 10)
        self.display_text("El objetivo del juego es ayudar a Scrat a tomar", 20, BLUE, 190, 150)
        self.display_text("las bellotas, evitando que el meteorito caiga sobre él", 20, BLUE, 180, 170)
        self.display_text("MECANICA:", 23, BLACK, 1030, 355)
        self.display_text("Usa las teclas de movimiento para atrapar ", 23, WHITE, 925, 370)
        self.display_text("las bellotas y escapar del meteorito", 23, WHITE, 950, 385)
        self.display_text("Highscore: " + (str(self.highscoretop)) , 36, WHITE, WIDTH// 2, 550)

        pygame.display.flip()

        self.wait()

    def wait(self):
        wait = True

        while wait:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type ==pygame.KEYUP:
                    wait = False



