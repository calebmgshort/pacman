import pygame
from constants import *
import public_vars
from objects import Wall

def create_map():
    walls = []
    # Wall(x, y, orientation, thickness, length)
    # Horizontal Walls
    # WALL_LATITUDE_1
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_1, Orientation.HORIZONTAL, WALL_LATITUDE_1_THICKNESS, WALL_HORIZONTAL_LENGTH_1))
    # WALL_LATITUDE_2
    walls.append(Wall(WALL_LONGITUDE_1+THIN_WALL_THICKNESS+LANE_SIZE, WALL_LATITUDE_2, Orientation.HORIZONTAL, WALL_LATITUDE_2_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    walls.append(Wall(WALL_LONGITUDE_3, WALL_LATITUDE_2, Orientation.HORIZONTAL, WALL_LATITUDE_2_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_6-WALL_LONGITUDE_6_THICKNESS, WALL_LATITUDE_2, Orientation.HORIZONTAL, WALL_LATITUDE_2_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_2, Orientation.HORIZONTAL, WALL_LATITUDE_2_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    # WALL_LATITUDE_3
    walls.append(Wall(WALL_LONGITUDE_1+THIN_WALL_THICKNESS+LANE_SIZE, WALL_LATITUDE_3, Orientation.HORIZONTAL, WALL_LATITUDE_3_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_3, Orientation.HORIZONTAL, WALL_LATITUDE_3_THICKNESS, WALL_HORIZONTAL_LENGTH_4))
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_3, Orientation.HORIZONTAL, WALL_LATITUDE_3_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    # WALL_LATITUDE_4
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_4, Orientation.HORIZONTAL, WALL_LATITUDE_4_OUTSIDE_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    walls.append(Wall(WALL_LONGITUDE_3, WALL_LATITUDE_4, Orientation.HORIZONTAL, WALL_LATITUDE_4_INSIDE_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_6-WALL_LONGITUDE_6_THICKNESS, WALL_LATITUDE_4, Orientation.HORIZONTAL, WALL_LATITUDE_4_INSIDE_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_4, Orientation.HORIZONTAL, WALL_LATITUDE_4_OUTSIDE_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    # WALL_LATITUDE_5
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_5_OUTSIDE, Orientation.HORIZONTAL, WALL_LATITUDE_5_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_5_INSIDE, Orientation.HORIZONTAL, WALL_LATITUDE_5_THICKNESS, WALL_HORIZONTAL_LENGTH_4))    
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_5_OUTSIDE, Orientation.HORIZONTAL, WALL_LATITUDE_5_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    # WALL_LATITUDE_6
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_6_OUTSIDE, Orientation.HORIZONTAL, WALL_LATITUDE_6_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_6_INSIDE, Orientation.HORIZONTAL, WALL_LATITUDE_6_THICKNESS, WALL_HORIZONTAL_LENGTH_4))    
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_6_OUTSIDE, Orientation.HORIZONTAL, WALL_LATITUDE_6_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    # WALL_LATITUDE_7
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_7_OUTSIDE, Orientation.HORIZONTAL, WALL_LATITUDE_7_OUTSIDE_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_7_INSIDE, Orientation.HORIZONTAL, WALL_LATITUDE_7_INSIDE_THICKNESS, WALL_HORIZONTAL_LENGTH_4))    
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_7_OUTSIDE, Orientation.HORIZONTAL, WALL_LATITUDE_7_OUTSIDE_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    # WALL_LATITUDE_8
    walls.append(Wall(WALL_LONGITUDE_1+THIN_WALL_THICKNESS+LANE_SIZE, WALL_LATITUDE_8, Orientation.HORIZONTAL, WALL_LATITUDE_8_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    walls.append(Wall(WALL_LONGITUDE_3, WALL_LATITUDE_8, Orientation.HORIZONTAL, WALL_LATITUDE_8_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_6-WALL_LONGITUDE_6_THICKNESS, WALL_LATITUDE_8, Orientation.HORIZONTAL, WALL_LATITUDE_8_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_8, Orientation.HORIZONTAL, WALL_LATITUDE_8_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    # WALL_LATITUDE_9
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_9, Orientation.HORIZONTAL, WALL_LATITUDE_9_THICKNESS, WALL_HORIZONTAL_LENGTH_6))
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_9, Orientation.HORIZONTAL, WALL_LATITUDE_9_THICKNESS, WALL_HORIZONTAL_LENGTH_4))
    walls.append(Wall(WALL_LONGITUDE_9-THIN_WALL_THICKNESS-LANE_SIZE, WALL_LATITUDE_9, Orientation.HORIZONTAL, WALL_LATITUDE_9_THICKNESS, WALL_HORIZONTAL_LENGTH_6))   
    # WALL_LATITUDE_10
    walls.append(Wall(WALL_LONGITUDE_1+THIN_WALL_THICKNESS+LANE_SIZE, WALL_LATITUDE_10, Orientation.HORIZONTAL, WALL_LATITUDE_10_THICKNESS, WALL_HORIZONTAL_LENGTH_7))
    walls.append(Wall(WALL_LONGITUDE_6-WALL_LONGITUDE_6_THICKNESS, WALL_LATITUDE_10, Orientation.HORIZONTAL, WALL_LATITUDE_10_THICKNESS, WALL_HORIZONTAL_LENGTH_7))
    # WALL_LATITUDE_11
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_11, Orientation.HORIZONTAL, WALL_LATITUDE_11_THICKNESS, WALL_HORIZONTAL_LENGTH_1))

    # TODO: Add vertical walls
    return walls