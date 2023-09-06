import pygame

pygame.init()

# Create the window
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Pygame Pong")
clock = pygame.time.Clock()

# Set variable for running the game
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


# Main program loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, "white", (player_pos, player_pos, player_pos, player_pos))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 100
    if keys[pygame.K_s]:
        player_pos.y += 100

    pygame.display.flip() 
