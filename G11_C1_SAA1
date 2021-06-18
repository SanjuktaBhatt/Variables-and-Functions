import pygame

pygame.init()

screen = pygame.display.set_mode((400,600))

paddle=pygame.Rect(200,500,30,30)
ball=pygame.Rect(70,50,10,10)


while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.draw.rect(screen,(23,100,100),paddle)
    pygame.draw.rect(screen,(255,69,0),ball)
    pygame.display.update()
