import constants
import math
def opposite_direction(direction):
    if direction == constants.Direction.RIGHT:
        return constants.Direction.LEFT
    elif direction == constants.Direction.LEFT:
        return constants.Direction.RIGHT
    elif direction == constants.Direction.UP:
        return constants.Direction.DOWN
    elif direction == constants.Direction.DOWN:
        return constants.Direction.UP
    else:
        raise ValueError("The direction is not a valid enum value")

def distance(point1, point2):
    leg1 = abs(point1[0] - point2[0])
    leg2 = abs(point1[1] - point2[1])
    return math.sqrt(leg1**2 + leg2**2)