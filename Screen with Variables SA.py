import pygame

pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)


score=0
#Create a variable lives=3



size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill(DARKBLUE)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    text = font.render("Lives: " + str(3), 1, WHITE)
    screen.blit(text, (500,10)) 
    screen.blit(text, (20,10))
    
    pygame.display.flip()