import pygame
import constants
import public_vars
import objects
import init
import time

# Initialize pygame
pygame.init()
# Initialize text
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 30)

# Create the screen
public_vars.screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

# Title
pygame.display.set_caption("Pacman")


# Pacman
pacman = objects.Pacman(constants.SCREEN_WIDTH//2-constants.CHARACTER_SIZE//2, constants.WALL_LATITUDE_8+constants.MEDIUM_WALL_THICKNESS, constants.Direction.LEFT)
red_ghost = objects.Ghost(constants.SCREEN_WIDTH//2-constants.CHARACTER_SIZE//2, constants.SCREEN_HEIGHT//2-constants.CHARACTER_SIZE//2, constants.Direction.DOWN, "resources/red.png")
green_ghost = objects.Ghost(constants.SCREEN_WIDTH//2+constants.CHARACTER_SIZE//2, constants.SCREEN_HEIGHT//2-constants.CHARACTER_SIZE//2, constants.Direction.RIGHT, "resources/green.png")
pink_ghost = objects.Ghost(constants.SCREEN_WIDTH//2-constants.CHARACTER_SIZE//2-constants.CHARACTER_SIZE, constants.SCREEN_HEIGHT//2-constants.CHARACTER_SIZE//2, constants.Direction.LEFT, "resources/pink.png")
orange_ghost = objects.Ghost(constants.SCREEN_WIDTH//2-constants.CHARACTER_SIZE//2, constants.SCREEN_HEIGHT//2-constants.CHARACTER_SIZE//2-constants.CHARACTER_SIZE, constants.Direction.UP, "resources/orange.png")


# Walls
public_vars.walls = init.generate_walls()

# Points
public_vars.points = init.generate_points()

# Score 
public_vars.score = 0

# Start time
public_vars.start_time = time.time()

def handle_keystroke(key):
    global pacman
    if key == pygame.K_LEFT:
        pacman.desired_direction = constants.Direction.LEFT
    elif key == pygame.K_RIGHT:
        pacman.desired_direction = constants.Direction.RIGHT
    elif key == pygame.K_UP:
        pacman.desired_direction = constants.Direction.UP
    elif key == pygame.K_DOWN:
        pacman.desired_direction = constants.Direction.DOWN


# Game loop
running = True
while running:
    public_vars.screen.fill(constants.BLACK)
    pacman.move()
    red_ghost.move()
    green_ghost.move()
    pink_ghost.move()
    orange_ghost.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            handle_keystroke(event.key)
    pacman.render()
    red_ghost.render()
    green_ghost.render()
    pink_ghost.render()
    orange_ghost.render()
    for wall in public_vars.walls:
        wall.render()
    for point in public_vars.points:
        point.render()
    textsurface = font.render('Score: {}'.format(public_vars.score), True, constants.WHITE)
    public_vars.screen.blit(textsurface, (constants.SCREEN_WIDTH/2,0))
    pygame.display.update()