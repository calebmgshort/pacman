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
# pacman_initial_image = pygame.image.load("resources/pacman.png")
# pacman_image = pygame.transform.scale(pacman_initial_image, (constants.CHARACTER_SIZE,constants.CHARACTER_SIZE))
# x = 300
# y = 400
# speed = 0.2
# pacman_direction = constants.Direction.RIGHT

# Walls
wall = objects.Wall(screen, 500, 300, constants.Orientation.VERTICAL, 200)

# def overlapping_horizontal(wall):
#     pacman_left = x
#     pacman_right = x + constants.CHARACTER_SIZE
#     # Pacman's edge is within wall's frame
#     if (pacman_left < wall.right and pacman_left > wall.left) or (pacman_right < wall.right and pacman_right > wall.left):
#         return True
#     # Wall's edge is withing pacman's frame
#     if (wall.left < pacman_right and wall.left > pacman_left) or (wall.right < pacman_right and wall.right > pacman_left):
#         return True
#     return False

# def overlapping_vertical(wall):
#     pacman_top = y
#     pacman_bottom = y + constants.CHARACTER_SIZE
#     # Pacman's edge is within wall's frame
#     if (pacman_top < wall.bottom and pacman_top > wall.top) or (pacman_bottom < wall.bottom and pacman_bottom > wall.top):
#         return True
#     # Wall's edge is withing pacman's frame
#     if (wall.top < pacman_bottom and wall.top > pacman_top) or (wall.bottom < pacman_bottom and wall.bottom > pacman_top):
#         return True
#     return False

# def overlapping(wall):
#     return overlapping_horizontal(wall) and overlapping_vertical(wall)

# def move():
#     global x, y, speed, wall
#     old_x = x
#     old_y = y
#     if pacman_direction == constants.Direction.RIGHT:
#         x += speed
#     elif pacman_direction == constants.Direction.LEFT:
#         x -= speed
#     elif pacman_direction == constants.Direction.UP:
#         y -= speed
#     elif pacman_direction == constants.Direction.DOWN:
#         y += speed
#     # Handle the case where we've reached the edge of the screen
#     if x < 0:
#         x = 0
#     if x > constants.SCREEN_WIDTH - constants.CHARACTER_SIZE:
#         x = constants.SCREEN_WIDTH - constants.CHARACTER_SIZE
#     if y < 0:
#         y = 0
#     if y > constants.SCREEN_HEIGHT - constants.CHARACTER_SIZE:
#         y = constants.SCREEN_HEIGHT - constants.CHARACTER_SIZE
#     # Handle the case where we've run into a wall
#     if overlapping(wall):
#         x = old_x
#         y = old_y


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