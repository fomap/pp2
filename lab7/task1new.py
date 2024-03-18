import pygame
import datetime
pygame.init()

w = 829
h = 826
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Mickey Mouse Clock")
clock = pygame.time.Clock()
FPS = 60
done = False

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)



minuteimg = pygame.image.load('lab7/img/left-hand.png')
wmin, hmin = minuteimg.get_size()
secimg = pygame.image.load('lab7/img/right-hand.png')
wsec, hsec = secimg.get_size()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    currtime = datetime.datetime.now()
    seconds = currtime.second
    minute = currtime.minute
    hour = currtime.hour
    pos = (screen.get_width()/2, screen.get_height()/2)
    screen.blit(pygame.image.load("lab7/img/main-clock.png"), (0,0))
    thetasec =  seconds*(360/60)
    thetamin = (minute + seconds/60)*(360/60)
    blitRotate(screen, minuteimg, pos, (wmin/2, hmin/2), -(thetamin-90)) 
    blitRotate(screen, secimg, pos, (wsec/2, hsec/2), -(thetasec-90)) 
    pygame.display.update()
    clock.tick(FPS)