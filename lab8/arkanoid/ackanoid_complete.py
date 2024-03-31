import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 200
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 15
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('audio/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 

unbreakNumbers = set()
for i in range (0, 10):
    randomNum = random.randrange(0, 40)
    unbreakNumbers.add(randomNum)

radiusBuff = set()
for i in range(0, 5):
    rand = random.randrange(0, 40)
    if rand not in unbreakNumbers:
        radiusBuff.add(rand)

widthBuff = set()
for i in range(0, 5):
    rand = random.randrange(0, 40)
    if rand not in unbreakNumbers and rand not in radiusBuff: #created so that every block that has buff in unique
        widthBuff.add(rand)

for i in unbreakNumbers:
    color_list[i] = (133, 133, 133)
    print(i)
for i in radiusBuff:
    color_list[i] = (255, 0, 0)
for i in widthBuff:
    color_list[i] = (255, 255, 255)


#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)



while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] 
  
    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    #Collision left & right
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision with blocks
    hitIndex = ball.collidelist(block_list) 
    if hitIndex != -1:
        if color_list[hitIndex] == (133, 133, 133): #if block is gray (unbreakable) then we just need to change direction of a ball
            dy = -dy
        else:
            if color_list[hitIndex] == (255, 0, 0):  #radius buff
                ballRadius += 2
            elif color_list[hitIndex] == (255, 255, 255): # paddle width buff
                paddleW += 20
            if paddleW > 50:
                paddleW = paddleW - 5
            ballSpeed += 0.5
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()

        
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    #overriding width and collider
    pygame.draw.rect(screen, (255,255,255), (paddle.x, paddle.y, paddleW, paddleH))
    paddle =  pygame.Rect(paddle.x, paddle.y, paddleW, paddleH)  
    #overriding radius
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
  
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list) - len(unbreakNumbers):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)

    pygame.display.flip()
    clock.tick(FPS)