# Import pygame library
import pygame

# Initialze pygame
pygame.init() 

# Create a variable named "WHITE" and assign RGB combination for white color to it.
WHITE = (255,255,255)

# Create a variable named "DARKBLUE" and assign RGB combination for darkblue color to it.
DARKBLUE = (36,90,190)

# Create a variable named "LIGHTBLUE" and assign RGB combination for lightblue color to it.
LIGHTBLUE = (0,176,240)

# Set the width and height of the game screen as 600 each.
size = (600,600)

# Create the game screen
screen = pygame.display.set_mode(size)

# Set the title of the game screen as "Breakout Game"
pygame.display.set_caption("Breakout Game")

# Create a rectangle for paddle object at coordinates (300,500), with width=60 and height=10
paddle = pygame.Rect(300,500,60,10)

# Create a rectangle for ball object at coordinates (200,250), with width=10 and height=10
ball = pygame.Rect(200,250,10,10)

# Create variables "ballx" and "bally" and assign the value 1 to both



# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # Check if user clicked on close
                  carryOn = False # Flag that we are done so we exit this loop             
    
    # Set the color of the screen to "DARKBLUE"
    screen.fill(DARKBLUE)
    
    # Draw the paddle on screen, set its color to "LIGHTBLUE"
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    
    # Update varaibles "ballx" and "bally" to update the position of the ball 
    
    
    
    # Draw the ball on screen, set its color to "WHITE"
    pygame.draw.rect(screen,WHITE ,ball)
    
    # Update x and y positions of the ball every 20 seconds
    pygame.time.wait(20)
    
    # Update the contents of the entire display
    pygame.display.flip()

# Quit the game
pygame.quit()
