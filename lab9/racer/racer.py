#Imports
import pygame, sys
from pygame.locals import *
import random, time


pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400  
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 25)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")
#creating mixer to play soundc cue
collision_sound = pygame.mixer.Sound('catch.mp3')


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] and self.rect.bottom < SCREEN_HEIGHT-5:
            self.rect.move_ip(0,5)
        if self.rect.left > 10:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH-10:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
#creating coin class, adding sprite and rect components, move method is just spawing sprite at random location
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #randomly chose between 2 types of coins
        self.randcoin = ["coin.png", "coin2.png"]
        self.res = random.choice(self.randcoin)
        self.image = pygame.image.load(self.res)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100,SCREEN_WIDTH-40), random.randint(100,SCREEN_HEIGHT-40))
   


#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
#Seperate sprite group was created to mimic way in which collision with other car occurs
coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)



#Game Loop
while True:
   
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

   
    DISPLAYSURF.blit(background, (0,0))
    
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (SCREEN_WIDTH-37, 10))
    DISPLAYSURF.blit(C1.image,C1.rect) #spawning coint
    
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    #on collision between player and coin just move coin to another location and inc score, also play sound so game feels less dead
    if pygame.sprite.spritecollideany(P1, coins):
        #identofying which coin we collide with, add SCORE accordingly
        if C1.res == "coin.png":
            SCORE += 2
        else:
            SCORE += 1
        
        if SCORE > 15:
            SPEED += 0.5

        C1.__init__()
        collision_sound.play()


    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
