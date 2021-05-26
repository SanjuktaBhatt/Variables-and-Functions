import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
bricksR=[pygame.Rect(10 + i* 100,60,80,30) for i in range(7)]
bricksO=[pygame.Rect(10 + i* 100,100,80,30) for i in range(7)]
bricksY=[pygame.Rect(10 + i* 100,140,80,30) for i in range(7)]
score = 0
lives = 3
velocity=[1,1]
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
paddle=pygame.Rect(300,500,60,10)
ball=pygame.Rect(200,250,10,10)
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [600, 38], 2)
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (500,10))   
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x<540: 
                paddle.x+=2
        if event.key == pygame.K_LEFT:
            if paddle.x>0:
                paddle.x-=2
    for i in bricksR:
        pygame.draw.rect(screen,RED,i)
    for i in bricksO:
        pygame.draw.rect(screen,ORANGE,i)   
    for i in bricksY:
        pygame.draw.rect(screen,YELLOW,i)      
    ball.x+=velocity[0]
    ball.y+=velocity[1]      
    if ball.x>=590 or ball.x<=0:
        velocity[0] = -velocity[0]
    if ball.y<=38 :
        velocity[1] = -velocity[1]
    if paddle.collidepoint(ball.x,ball.y):
         velocity[1]=-velocity[1]
    if ball.y>=590:
        lives-=1
        font = pygame.font.Font(None, 74)
        text = font.render("LOST A  LIFE", 1, WHITE)
        screen.blit(text, (150,250))
        font = pygame.font.Font(None, 34)
        text = font.render("Lives left:"+str(lives), 1, WHITE)
        screen.blit(text, (150,300))
        pygame.display.flip()
        ball.x=200
        ball.y=250
        pygame.time.wait(1000)
    pygame.draw.rect(screen,WHITE ,ball)
    #score
    for i in bricksR:
        if i.collidepoint(ball.x,ball.y):
            bricksR.remove(i)
            velocity[0] = -velocity[0]
            velocity[1]=-velocity[1]
            score+=3
    for i in bricksO:
        if i.collidepoint(ball.x,ball.y):
            bricksO.remove(i)
            velocity[0] = -velocity[0]
            velocity[1]=-velocity[1]
            score+=2
    for i in bricksY:
        if i.collidepoint(ball.x,ball.y):
            velocity[0] = -velocity[0]
            velocity[1]=-velocity[1]
            bricksY.remove(i)
            score+=1
    if lives==0:
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, RED)
        screen.blit(text, (150,350))
        pygame.display.flip()
        pygame.time.wait(2000)
        
    if score==36:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON!!", 1, RED)
        screen.blit(text, (150,350))
        pygame.display.flip()
        pygame.time.wait(2000)
        break
    pygame.time.wait(1)
    pygame.display.flip()       
pygame.quit(  )

