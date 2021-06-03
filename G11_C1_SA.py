import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill(DARKBLUE)
    paddle=pygame.Rect(300,500,60,10)
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    #Add ball here
    
    
    pygame.display.flip()
pygame.quit()
    
