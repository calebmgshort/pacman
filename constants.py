from enum import Enum


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

class Orientation(Enum):
    HORIZONTAL = 0
    VERTICAL = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_SIZE = 40
WALL_THICKNESS = 10

BLACK = (0,0,0)
BLUE = (0,0,255)
