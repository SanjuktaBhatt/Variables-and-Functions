import pygame

pygame.init()

screen = pygame.display.set_mode((400,600))
#Create the apddle here


while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #Draw the paddle here
    
    pygame.display.update()
