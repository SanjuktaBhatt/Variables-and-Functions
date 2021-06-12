import pygame
pygame.init() 



screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Breakout Game")
paddle=pygame.Rect(300,500,60,10)
ball=pygame.Rect(200,250,10,10)
ballx=-1
bally=-1
paddlex=2
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill((36,90,190))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x<540: 
                paddle.x+=paddlex
        if event.key == pygame.K_LEFT:
            if paddle.x>0:
                paddle.x-=paddlex
           
    pygame.draw.rect(screen,(0,176,240),paddle)
    ball.x=ball.x+ballx
    ball.y=ball.y+bally
    if ball.x>=590:
        ballx=-ballx
    if ball.x<=10:
        ballx=-ballx
    if ball.y>=590:
        bally=-bally
    if ball.y<=10:
        bally=-bally
    if paddle.collidepoint(ball.x,ball.y):
        bally=-bally
   
    pygame.draw.rect(screen,(255,255,255) ,ball)
    
    for i in range(7):
     brick=pygame.Rect(10 + i* 100,60,80,30)
      pygame.draw.rect(screen,(255,0,0),brick)
    #Create orange brick here
    
    pygame.display.flip()
pygame.quit()
    
