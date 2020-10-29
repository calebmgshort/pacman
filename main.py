import pygame
import constants
import public_vars
import objects
import init
import time
from ghost_algorithms import *

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
# TODO: Write ghost destination algorithm
public_vars.pacman = objects.Pacman(constants.SCREEN_WIDTH/2-constants.CHARACTER_SIZE/2, constants.WALL_LATITUDE_8+constants.MEDIUM_WALL_THICKNESS, constants.Direction.LEFT)
public_vars.red_ghost = objects.Ghost("red", constants.SCREEN_WIDTH/2-constants.CHARACTER_SIZE/2, constants.SCREEN_HEIGHT/2-constants.CHARACTER_SIZE/2-constants.CHARACTER_SIZE, constants.Direction.UP, "resources/red.png", destination_red)
public_vars.green_ghost = objects.Ghost("green", constants.SCREEN_WIDTH/2+constants.CHARACTER_SIZE/2, constants.SCREEN_HEIGHT/2-constants.CHARACTER_SIZE/2, constants.Direction.LEFT, "resources/green.png", destination_green)
public_vars.pink_ghost = objects.Ghost("pink", constants.SCREEN_WIDTH/2-constants.CHARACTER_SIZE/2-constants.CHARACTER_SIZE, constants.SCREEN_HEIGHT/2-constants.CHARACTER_SIZE/2, constants.Direction.LEFT, "resources/pink.png", destination_pink)
public_vars.orange_ghost = objects.Ghost("orange", constants.SCREEN_WIDTH/2-constants.CHARACTER_SIZE/2, constants.SCREEN_HEIGHT/2-constants.CHARACTER_SIZE/2, constants.Direction.UP, "resources/orange.png", destination_orange)


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
        public_vars.pacman.desired_direction = constants.Direction.LEFT
    elif key == pygame.K_RIGHT:
        public_vars.pacman.desired_direction = constants.Direction.RIGHT
    elif key == pygame.K_UP:
        public_vars.pacman.desired_direction = constants.Direction.UP
    elif key == pygame.K_DOWN:
        public_vars.pacman.desired_direction = constants.Direction.DOWN


# Game loop
running = True
while running:
    public_vars.screen.fill(constants.BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            handle_keystroke(event.key)
    public_vars.pacman.move()
    public_vars.red_ghost.move()
    public_vars.green_ghost.move()
    public_vars.pink_ghost.move()
    public_vars.orange_ghost.move()
    public_vars.pacman.render()
    for point in public_vars.points:
        point.render()
    public_vars.red_ghost.render()
    public_vars.green_ghost.render()
    public_vars.pink_ghost.render()
    public_vars.orange_ghost.render()
    for wall in public_vars.walls:
        wall.render()
    textsurface = font.render('Score: {}'.format(public_vars.score), True, constants.WHITE)
    public_vars.screen.blit(textsurface, (constants.SCREEN_WIDTH/2,0))
    pygame.display.update()