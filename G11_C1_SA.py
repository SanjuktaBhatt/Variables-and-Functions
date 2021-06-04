import pygame

pygame.init()

screen = pygame.display.set_mode((400,600))

paddle=pygame.Rect(200,500,30,30)
#create a ball here


while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.draw.rect(screen,(23,100,100),paddle)
    #draw the ball here
    
    pygame.display.update()
