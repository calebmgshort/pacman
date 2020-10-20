from enum import Enum


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

class Orientation(Enum):
    HORIZONTAL = 0
    VERTICAL = 1

# Default settings
CHARACTER_SPEED = 0.2
THIN_WALL_THICKNESS = 10
MEDIUM_WALL_THICKNESS = 2 * THIN_WALL_THICKNESS
THICK_WALL_THICKNESS = 4 * THIN_WALL_THICKNESS
LANE_SIZE = 4 * THIN_WALL_THICKNESS
CHARACTER_SIZE = LANE_SIZE - LANE_SIZE//10

# Colors
BLACK = (0,0,0)
BLUE = (0,0,255)

# Board Settings
# screen height = 10 lanes + 4 thin walls + 6 medium walls + 1 thick wall, + 4 outside lanes
SCREEN_HEIGHT = 10*LANE_SIZE + 4*THIN_WALL_THICKNESS + 6*MEDIUM_WALL_THICKNESS + 1*THICK_WALL_THICKNESS + 4*LANE_SIZE
# screen width = 10 lanes + 2 thin walls + 7 medium walls, + 2 outside lanes
SCREEN_WIDTH = 10*LANE_SIZE + 2*THIN_WALL_THICKNESS + 7*MEDIUM_WALL_THICKNESS + 2*LANE_SIZE

# Horizontal, lattitudal walls
# Upper Walls
WALL_LATITUDE_1 = 2 * LANE_SIZE
WALL_LATITUDE_2 = WALL_LATITUDE_1 + THIN_WALL_THICKNESS + LANE_SIZE
WALL_LATITUDE_3 = WALL_LATITUDE_2 + THICK_WALL_THICKNESS + LANE_SIZE
WALL_LATITUDE_4 = WALL_LATITUDE_3 + MEDIUM_WALL_THICKNESS + LANE_SIZE
# Middle Walls
WALL_LATITUDE_5_OUTSIDE = WALL_LATITUDE_4 + MEDIUM_WALL_THICKNESS + LANE_SIZE + THIN_WALL_THICKNESS
WALL_LATITUDE_5_INSIDE = WALL_LATITUDE_4 + MEDIUM_WALL_THICKNESS + LANE_SIZE
WALL_LATITUDE_6_OUTSIDE = WALL_LATITUDE_5_OUTSIDE + THIN_WALL_THICKNESS + LANE_SIZE
WALL_LATITUDE_6_INSIDE = WALL_LATITUDE_6_OUTSIDE + THIN_WALL_THICKNESS
# Lower Walls
WALL_LATITUDE_7_INSIDE = WALL_LATITUDE_6_INSIDE + THIN_WALL_THICKNESS + LANE_SIZE
WALL_LATITUDE_7_OUTSIDE = WALL_LATITUDE_7_INSIDE + THIN_WALL_THICKNESS
WALL_LATITUDE_8 = WALL_LATITUDE_7_OUTSIDE + THIN_WALL_THICKNESS + LANE_SIZE
WALL_LATITUDE_9 = WALL_LATITUDE_8 + MEDIUM_WALL_THICKNESS + LANE_SIZE
WALL_LATITUDE_10 = WALL_LATITUDE_9 + MEDIUM_WALL_THICKNESS + LANE_SIZE
WALL_LATITUDE_11 = WALL_LATITUDE_10 + MEDIUM_WALL_THICKNESS + LANE_SIZE

# Vertical, longitudal walls
# Leftern Walls
WALL_LONGITUDE_1 = 1 * LANE_SIZE
WALL_LONGITUDE_2_OUTER = WALL_LONGITUDE_1 + THIN_WALL_THICKNESS + 2*LANE_SIZE
WALL_LONGITUDE_2_INNER = WALL_LONGITUDE_2_OUTER + THIN_WALL_THICKNESS
WALL_LONGITUDE_3 = WALL_LONGITUDE_2_OUTER + MEDIUM_WALL_THICKNESS + LANE_SIZE
WALL_LONGITUDE_4 = WALL_LONGITUDE_3 + MEDIUM_WALL_THICKNESS + LANE_SIZE
# Middle Wall
WALL_LONGITUDE_5 = WALL_LONGITUDE_4 + MEDIUM_WALL_THICKNESS + LANE_SIZE
# Rightern Walls
WALL_LONGITUDE_6 = WALL_LONGITUDE_5 + MEDIUM_WALL_THICKNESS + LANE_SIZE + THIN_WALL_THICKNESS
WALL_LONGITUDE_7 = WALL_LONGITUDE_6 + THIN_WALL_THICKNESS + LANE_SIZE
WALL_LONGITUDE_8 = WALL_LONGITUDE_7 + MEDIUM_WALL_THICKNESS + LANE_SIZE
WALL_LONGITUDE_9 = WALL_LONGITUDE_8 + MEDIUM_WALL_THICKNESS + 2*LANE_SIZE


# All Wall Lengths
# 7 Horizontal wall lengths
WALL_HORIZONTAL_LENGTH_1 = WALL_LONGITUDE_9 - WALL_LONGITUDE_1 + THIN_WALL_THICKNESS
WALL_HORIZONTAL_LENGTH_2 = (WALL_LONGITUDE_2_INNER + THIN_WALL_THICKNESS) - (WALL_LONGITUDE_1 + THIN_WALL_THICKNESS + LANE_SIZE)
WALL_HORIZONTAL_LENGTH_3 = (WALL_LONGITUDE_5-LANE_SIZE) - WALL_LONGITUDE_3 
WALL_HORIZONTAL_LENGTH_4 = (WALL_LONGITUDE_6 + THIN_WALL_THICKNESS) - WALL_LONGITUDE_4
WALL_HORIZONTAL_LENGTH_5 = (WALL_LONGITUDE_2_INNER + THIN_WALL_THICKNESS) - WALL_LONGITUDE_1
WALL_HORIZONTAL_LENGTH_6 = LANE_SIZE + THIN_WALL_THICKNESS
WALL_HORIZONTAL_LENGTH_7 = WALL_LONGITUDE_5 - WALL_LONGITUDE_1 - THIN_WALL_THICKNESS - 2*LANE_SIZE
# Vertical wall lengths
WALL_VERTICAL_LENGTH_1 = WALL_LATITUDE_4 + THIN_WALL_THICKNESS - WALL_LATITUDE_1
WALL_VERTICAL_LENGTH_2 = WALL_LATITUDE_11 + THIN_WALL_THICKNESS - WALL_LATITUDE_7_OUTSIDE
WALL_VERTICAL_LENGTH_3 = WALL_LATITUDE_5_OUTSIDE + THIN_WALL_THICKNESS - WALL_LATITUDE_4
WALL_VERTICAL_LENGTH_4 = WALL_LATITUDE_9 + MEDIUM_WALL_THICKNESS - WALL_LATITUDE_8
