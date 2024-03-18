import pygame

pygame.init()

width = 400

height = 300
screen = pygame.display.set_mode((width, height))

done = False

x = 200
y = 150
step = 20


clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    pressed = pygame.key.get_pressed()
   
    if pressed[pygame.K_LEFT] and x >step+25:
        x -= step
    if pressed[pygame.K_RIGHT] and x < width - 25 - step:
        x += step   
    if pressed[pygame.K_UP] and y > step + 25:
        y -= step
    if pressed[pygame.K_DOWN] and y < height - 25 - step:
        y += step
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255,0,0), (x,y),25)
    
    pygame.display.flip()
    clock.tick(60)