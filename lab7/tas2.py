import pygame
import os

pygame.init()
pygame.mixer.init()


width = 700
height = 500
screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
done = False


font = pygame.font.SysFont('comicsansms', 40)
text = font.render('P-play, S-stop, N-next, B-Previous', True, (255, 192, 203))
textRect = text.get_rect()
textRect.center = (width// 2, height // 2)

music = "D:\\UNI\\pp2\\lab7\\songs"
files = [file for file in os.listdir(music)]
current = 0
pygame.mixer.music.load(os.path.join(music, files[current]))



def nexttrack():
    global current
    if current < len(files) - 1:
        current += 1
    else:
        current = 0
    pygame.mixer.music.load(os.path.join(music, files[current]))
    pygame.mixer.music.play()

def previoustrack():
    global current
    if current > 0:
        current -= 1
    else:
        current = len(files) - 1
    pygame.mixer.music.load(os.path.join(music, files[current]))
    pygame.mixer.music.play()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((234, 250, 177))     
    screen.blit(text, textRect) 
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_s]:
        pygame.mixer.music.stop() 
    if pressed[pygame.K_p]:
        pygame.mixer.music.play()
    if pressed[pygame.K_n]:
        nexttrack()
    if pressed[pygame.K_b]:
        previoustrack()
    pygame.display.update()
  