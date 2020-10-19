import pygame
import constants
import public_vars
import objects
import init

# Initialize pygame
pygame.init()

# Create the screen
public_vars.screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

# Title
pygame.display.set_caption("Pacman")

# Pacman
pacman = objects.Character(0, 0, constants.Direction.RIGHT, "resources/pacman.png")

# Walls
walls = init.create_map()

def handle_keystroke(key):
    global pacman
    if key == pygame.K_LEFT:
        pacman.direction = constants.Direction.LEFT
    elif key == pygame.K_RIGHT:
        pacman.direction = constants.Direction.RIGHT
    elif key == pygame.K_UP:
        pacman.direction = constants.Direction.UP
    elif key == pygame.K_DOWN:
        pacman.direction = constants.Direction.DOWN


# Game loop
running = True
while running:
    public_vars.screen.fill(constants.BLACK)
    pacman.move(walls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            handle_keystroke(event.key)



    pacman.render()
    for wall in walls:
        wall.render()
    pygame.display.update()