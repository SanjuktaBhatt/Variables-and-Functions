import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
size=(600,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
paddle=pygame.Rect(300,500,60,10)
ball=pygame.Rect(200,250,10,10)
#Create ballx and bally here


carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill(DARKBLUE)
    
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    # Update ball movement here(before drawing the ball on the screen)
    
    
    pygame.draw.rect(screen,WHITE ,ball)
    pygame.time.wait(20)
    pygame.display.flip()
pygame.quit()
    
