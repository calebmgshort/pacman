import pygame
from enum import Enum
import constants

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

# Title
pygame.display.set_caption("Pacman")

class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

# Player
pacman_initial_image = pygame.image.load("resources/pacman.png")
pacman_image = pygame.transform.scale(pacman_initial_image, (constants.PACMAN_SIZE,constants.PACMAN_SIZE))
x = 300
y = 400
speed = 0.2
pacman_direction = Direction.RIGHT

def player(x, y):
    screen.blit(pacman_image, (x,y))

def calculate_velocity():
    global x, y, speed
    if pacman_direction == Direction.RIGHT:
        x += speed
    elif pacman_direction == Direction.LEFT:
        x -= speed
    elif pacman_direction == Direction.UP:
        y -= speed
    elif pacman_direction == Direction.DOWN:
        y += speed
    if x < 0:
        x = 0
    if x > constants.SCREEN_WIDTH - constants.PACMAN_SIZE:
        x = constants.SCREEN_WIDTH - constants.PACMAN_SIZE
    if y < 0:
        y = 0
    if y > constants.SCREEN_HEIGHT - constants.PACMAN_SIZE:
        y = constants.SCREEN_HEIGHT - constants.PACMAN_SIZE

def handle_keystroke(key):
    global pacman_direction
    if key == pygame.K_LEFT:
        pacman_direction = Direction.LEFT
    elif key == pygame.K_RIGHT:
        pacman_direction = Direction.RIGHT
    elif key == pygame.K_UP:
        pacman_direction = Direction.UP
    elif key == pygame.K_DOWN:
        pacman_direction = Direction.DOWN


# Game loop
running = True
while running:
    screen.fill((0,0,0))
    calculate_velocity()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            handle_keystroke(event.key)



    player(x, y)
    pygame.display.update()