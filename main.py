import pygame
import constants
import objects

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

# Title
pygame.display.set_caption("Pacman")

# Pacman
pacman = objects.Character(screen, 300, 400, constants.Direction.RIGHT, "resources/pacman.png")

# Walls
wall = objects.Wall(screen, 500, 300, constants.Orientation.VERTICAL, 200)

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
    screen.fill(constants.BLACK)
    pacman.move(wall)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            handle_keystroke(event.key)



    pacman.render()
    wall.render()
    pygame.display.update()