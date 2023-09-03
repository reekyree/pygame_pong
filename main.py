import pygame

pygame.init()

# Create the window
screen = pygame.display.set_mode((500, 400))

# Set the title of the window
pygame.display.set_caption("Pygame Pong")

# Set variable for running the game
running = True

# Main program loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
