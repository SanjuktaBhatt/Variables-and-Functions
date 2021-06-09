import pygame
pygame.init() 
screen = pygame.display.set_mode(600, 600)
box=pygame.Rect(300,500,60,10)

carryOn = True
while carryOn:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  carryOn = False            
    screen.fill((36,90,190))
 
    pygame.draw.rect(screen,(255, 192, 203),box)
    
    pygame.display.flip()
pygame.quit()
    
