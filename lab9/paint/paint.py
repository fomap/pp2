import pygame, time
pygame.init()



FPS = 100
time = pygame.time.Clock()

W = 800
H = 800
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

done = False
pygame.display.set_caption("Pretty paint")

rectangle = False
circle = False
rad = 15
pos = []
activeColor = (255, 255, 255)


def menu():
    pygame.draw.rect(screen, (242, 206, 219), [0, 0, W, 90])
    #colors
    red = pygame.draw.rect(screen, (255,179,186), [W - 120, 15, 27, 27])
    orange = pygame.draw.rect(screen, (255,223,186), [W - 90, 15, 27, 27])
    yellow = pygame.draw.rect(screen, (255,255,186), [W - 60, 15, 27, 27])
    green = pygame.draw.rect(screen, (186,255,201), [W - 120, 40, 27, 27])
    blue = pygame.draw.rect(screen, (186,225,255), [W - 90, 40, 27, 27])
    purple = pygame.draw.rect(screen, (173, 136, 198), [W - 60, 40, 27, 27])
    black = pygame.draw.rect(screen, (0,0, 0), [W - 150, 15, 27, 27])
    white = pygame.draw.rect(screen, (255, 255, 255), [W - 150, 40, 27, 27])
    colors = [red, orange, yellow, green, blue, purple, black, white]
    colorList = [(255,179,186), (255,223,186),(255,255,186), (186,255,201), (186,225,255), (173, 136, 198), (0,0, 0), (255, 255, 255)]

    return colors, colorList

def draw(list):
    for i in range(len(list)):
        pygame.draw.circle(screen, list[i][0], list[i][1], list[i][2])


while not done:
    
    screen.fill((255,255,255))
    colors, rgsList  = menu()
    mouse = pygame.mouse.get_pos()
    drawing = pygame.mouse.get_pressed()[0]
   

    if mouse[1] > 90:
        pygame.draw.circle(screen, activeColor, mouse, rad)
    if drawing and mouse[1] > 90:
        pos.append((activeColor, mouse, rad))
    
    draw(pos)  
         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
    
            #brush size
            if event.key == pygame.K_p:
                rad = min(200, rad + 1)
            if event.key == pygame.K_o: 
                rad = max(1, rad - 1)
            #clear canvas
            if event.key == pygame.K_e:
                pos.clear()



                  
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    activeColor = rgsList[i]
            

 
    
    pygame.display.flip()
  
    time.tick(FPS)