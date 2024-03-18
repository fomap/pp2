import pygame
import os
import datetime


imglib = {}

def getimg(path):
    global imglib
    image = imglib.get(path)
    if image == None:
        canonicalized_path  = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        imglib[path] = image
    return image


pygame.init()
width = 548
height = 548
screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
done = False
clock = pygame.time.Clock()


font = pygame.font.SysFont("comicsansms", 72)


def blitRotate(surf, image, pos, originPos, angle):

#offset pivot
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
  


try:
    image= pygame.image.load('/root/pp2/lab7/img/hand.jpg')
except:
    image = pygame.Surface()



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    current_time = datetime.datetime.now()
    screen.blit(getimg('/root/pp2/lab7/img/clock.png'),(0,0))       

    text = font.render("{}:{}:{}".format(current_time.hour, current_time.minute, current_time.second), True, (0, 128, 0))
    screen.blit(text,(width // 2, height // 2))
    #screen.fill((0,0,0))
    pygame.display.update()
    clock.tick(30)