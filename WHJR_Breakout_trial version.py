import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
bricks=[]
for j in ([60,100,140]):
  bricks.append([pygame.Rect(10 + i* 100,j,80,30) for i in range(7)])


def draw_brick():
    for i in bricks:
        for j in i:
            pygame.draw.rect(screen,RED,j)

score = 0
lives = 3
velocity=[1,1]
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
paddle=pygame.Rect(300,550,60,10) #(x,y,width,height)
ball=pygame.Rect(200,250,10,10)
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill(DARKBLUE)
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    #paddle movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x<540: 
                paddle.x+=5
        if event.key == pygame.K_LEFT:
            if paddle.x>0:
                paddle.x-=5
    # brick wall   
    draw_brick()
    
    
    #ball movement    
    ball.x+=velocity[0]
    ball.y+=velocity[1]  
    
    if ball.x>=590 or ball.x<=0:
        velocity[0] = -velocity[0]
    if ball.y<=38  :
        velocity[1] = -velocity[1]
    if paddle.collidepoint(ball.x,ball.y):
         velocity[1]=-velocity[1]
    if ball.y>=590:
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, RED)
        screen.blit(text, (150,350))
        pygame.display.flip()
        pygame.time.wait(2000)
        break
    pygame.draw.rect(screen,WHITE ,ball)
    #score
    for i in bricks:
        for j in i:
            if j.collidepoint(ball.x,ball.y):
                bricks.remove(j)
                velocity[0] = -velocity[0]
                velocity[1]=-velocity[1]
                score+=1
                
    if score==18:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON!!", 1, RED)
        screen.blit(text, (150,350))
        pygame.display.flip()
        pygame.time.wait(2000)
        break
    pygame.time.wait(1)
    pygame.display.flip()       
pygame.quit(  )

