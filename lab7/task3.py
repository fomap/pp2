import pygame

pygame.init()

width = 400

height = 300
screen = pygame.display.set_mode((width, height))

done = False

x = 150
y = 200
step = 3


clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y >  (30-step): y -= step
    if pressed[pygame.K_DOWN] and y < height - (30-step): y += step
    if pressed[pygame.K_LEFT] and x > (30-step): x -= step
    if pressed[pygame.K_RIGHT] and x < width- (30-step): x += step        
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255,0,0), (x,y),25)
    
    pygame.display.flip()
    clock.tick(60)