import pygame, time, math
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
activeTool = None
# initialpos = 0
# finalpos = 0
x = y = dx = dy = 0

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


    # Draw square
    square = pygame.draw.rect(screen,(242, 206, 219), [15, 15, 50, 50]) 
    pygame.draw.rect(screen, (255,255,255), [25,25,30,30])
    # Draw right triangle
    rightTriangle = pygame.draw.rect(screen,(242, 206, 219), [70, 15, 50, 50])
    pygame.draw.polygon(screen, (255,255,255), [(80, 25), (110, 55), (80, 55)]) 
    # # Draw equilateral triangle
    equilateralTriangle = pygame.draw.rect(screen,(242, 206, 219), [125, 15, 50, 50])
    pygame.draw.polygon(screen, (255,255,255), [(150, 20), (170, 55), (130, 55)])
    # # Draw rhombus
    rhombus = pygame.draw.rect(screen,(242, 206, 219), [180, 15, 50, 50]) 
    pygame.draw.polygon(screen, (255,255,255), [(185, 20), (205, 20), (220, 55), (200, 55)])
    # # Draw rectangle
    rectangle = pygame.draw.rect(screen,(242, 206, 219), [235, 15, 50, 50]) 
    pygame.draw.rect(screen, (255,255,255), [240, 30, 40,20 ])
    # # Draw circle
    circle = pygame.draw.rect(screen,(242, 206, 219), [290, 15, 50, 50]) 
    pygame.draw.circle(screen, (255,255,255), (315,40), 20)

    toolList = square, rightTriangle, equilateralTriangle, rhombus, rectangle, circle

    return colors, colorList, toolList

def draw(list):
    for i in range(len(list)):
        pygame.draw.circle(screen, list[i][0], list[i][1], list[i][2])


while not done:
    
    screen.fill((255,255,255))
    colors, rgsList, tools  = menu()
    mouse = pygame.mouse.get_pos()
    drawing = pygame.mouse.get_pressed()[0]
   

         
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
            if event.key == pygame.K_b:
                activeTool = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(tools)):
                if tools[i].collidepoint(event.pos):
                    activeTool = i 
                    # print(activeTool)
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    activeColor = rgsList[i]

            
            x, y = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            dx, dy= event.pos
        
    #square, rightTriangle, equilateralTriangle, rhombus, rectangle, circle
    if activeTool == 0: #square,
        pygame.draw.rect(screen, activeColor, [x,y,dx,dx])
        pos.clear()
    if activeTool == 1: #rightTriangle
        pygame.draw.polygon(screen,activeColor, [(x,y),(dx, dy),(dx, y)])
        pos.clear()
    if activeTool == 2: #equilateralTriangle
        a1 = x
        b1 = y
        a2 = dx
        b2 = dy

        distance = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)
        angle = math.atan2(b2 - b1, a2 - a1)
        a3 = a1 + distance * math.cos(angle - (1 * math.pi / 3))
        b3 = b1 + distance * math.sin(angle - (1 * math.pi / 3))
       
        pygame.draw.polygon(screen,activeColor, [(a1,b1),(a2, b2),(a3, b3)])
        pos.clear()
    if activeTool == 3:# rhombus
        pygame.draw.polygon(screen,activeColor, [(x +100, y),(x + dx + 100, y),(x + dx, y+ dy),(x, y +dy)])
        pos.clear()
    if activeTool == 4: #rectangle
        pygame.draw.rect(screen, activeColor, [x,y,dx,dy])
        pos.clear()
    if activeTool == 5: #circle
        pygame.draw.circle(screen,activeColor, (x,y), dx)
        pos.clear()

   
    if mouse[1] > 90:
        pygame.draw.circle(screen, activeColor, mouse, rad)
    if drawing and mouse[1] > 90:
        pos.append((activeColor, mouse, rad))
    
    draw(pos)  
            

 
    
    pygame.display.flip()
  
    time.tick(FPS)