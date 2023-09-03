import pygame

pygame.init()

# Create the window
screen = pygame.display.set_mode((500, 400))

# Set the title of the window
pygame.display.set_caption("Pygame Pong")

# Draw a rectangle to the screen
pygame.draw.rect(screen, "white", (50, 50, 100, 100))

# Update the screen
pygame.display.flip()

# Set variable for running the game
running = True

# Main program loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
