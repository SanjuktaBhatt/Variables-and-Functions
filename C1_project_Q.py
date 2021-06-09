import pygame
pygame.init() 
screen = pygame.display.set_mode(600, 600)

#Create the box here


carryOn = True
while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False           
    screen.fill((36,90,190))
    
    #Draw the box here
    
    
    pygame.display.flip()
pygame.quit()
    
