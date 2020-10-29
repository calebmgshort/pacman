from constants import *
import public_vars
from util import distance
from math import sqrt
from random import random

# Red hunts. Goes straight for pacman
def destination_red():
    return (public_vars.pacman.x, public_vars.pacman.y)

# Pink ambushes. Goes 4 lanes in head of pacman
def destination_pink():
    if public_vars.pacman.direction == Direction.RIGHT:
        return (public_vars.pacman.x + 4 * LANE_SIZE, public_vars.pacman.y)
    elif public_vars.pacman.direction == Direction.LEFT:
        return (public_vars.pacman.x - 4 * LANE_SIZE, public_vars.pacman.y)
    elif public_vars.pacman.direction == Direction.UP:
        return (public_vars.pacman.x, public_vars.pacman.y - 4*LANE_SIZE)
    elif public_vars.pacman.direction == Direction.DOWN:
        return (public_vars.pacman.x, public_vars.pacman.y + 4*LANE_SIZE)
    else:
        raise ValueError("The direction provided is not valid")
    raise ValueError("This statement should never be reached! And the direction provided is not valid")

# Green goes to the point accross pacman from red
def destination_green():
    x_dif = public_vars.pacman.x - public_vars.red_ghost.x
    y_dif = public_vars.pacman.y - public_vars.red_ghost.y
    return (public_vars.pacman.x + x_dif, public_vars.pacman.y + y_dif)

# Orange hunts like red, unless it's too close, in which case it picks a random spot. 
def destination_orange():
    if distance((public_vars.orange_ghost.x, public_vars.orange_ghost.y), (public_vars.pacman.x, public_vars.pacman.y)) > 4 * LANE_SIZE * sqrt(2):
        return destination_red()
    return (random() * SCREEN_WIDTH, random() * SCREEN_HEIGHT)

