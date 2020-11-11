import pygame
from constants import *
import public_vars
from objects import *
import time
import random
from valid_character_locations import ValidCharacterLocations
from typing import List

def generate_walls():
    walls = []
    # Wall(x, y, orientation, thickness, length)
    # Horizontal Walls
    # WALL_LATITUDE_1
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_1, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_1))
    # WALL_LATITUDE_2
    walls.append(Wall(WALL_LONGITUDE_1+THIN_WALL_THICKNESS+LANE_SIZE, WALL_LATITUDE_2, Orientation.HORIZONTAL, THICK_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    walls.append(Wall(WALL_LONGITUDE_3, WALL_LATITUDE_2, Orientation.HORIZONTAL, THICK_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_6-THIN_WALL_THICKNESS, WALL_LATITUDE_2, Orientation.HORIZONTAL, THICK_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_2, Orientation.HORIZONTAL, THICK_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    # WALL_LATITUDE_3
    walls.append(Wall(WALL_LONGITUDE_1+THIN_WALL_THICKNESS+LANE_SIZE, WALL_LATITUDE_3, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_3, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_4))
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_3, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    # WALL_LATITUDE_4
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_4, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    walls.append(Wall(WALL_LONGITUDE_3, WALL_LATITUDE_4, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_6-THIN_WALL_THICKNESS, WALL_LATITUDE_4, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_4, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    # WALL_LATITUDE_5
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_5_OUTSIDE, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_5_INSIDE, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_4//3))

    walls.append(Wall(WALL_LONGITUDE_4 + 2*WALL_HORIZONTAL_LENGTH_4//3, WALL_LATITUDE_5_INSIDE, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_4//3))    
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_5_OUTSIDE, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    # WALL_LATITUDE_6
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_6_OUTSIDE, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_6_INSIDE, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_4))    
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_6_OUTSIDE, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    # WALL_LATITUDE_7
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_7_OUTSIDE, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_7_INSIDE, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_4))    
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_7_OUTSIDE, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_5))
    # WALL_LATITUDE_8
    walls.append(Wall(WALL_LONGITUDE_1+THIN_WALL_THICKNESS+LANE_SIZE, WALL_LATITUDE_8, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    walls.append(Wall(WALL_LONGITUDE_3, WALL_LATITUDE_8, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_6-THIN_WALL_THICKNESS, WALL_LATITUDE_8, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_8, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_2))
    # WALL_LATITUDE_9
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_9, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_6))
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_9, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_4))
    walls.append(Wall(WALL_LONGITUDE_9-LANE_SIZE, WALL_LATITUDE_9, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_6))   
    # WALL_LATITUDE_10
    walls.append(Wall(WALL_LONGITUDE_1+THIN_WALL_THICKNESS+LANE_SIZE, WALL_LATITUDE_10, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_7))
    walls.append(Wall(WALL_LONGITUDE_6-THIN_WALL_THICKNESS, WALL_LATITUDE_10, Orientation.HORIZONTAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_7))
    # WALL_LATITUDE_11
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_11, Orientation.HORIZONTAL, THIN_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_1))

    # Add vertical walls
    # WALL_LONGITUDE_1
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_1, Orientation.VERTICAL, THIN_WALL_THICKNESS, WALL_VERTICAL_LENGTH_1))
    walls.append(Wall(WALL_LONGITUDE_1, WALL_LATITUDE_7_OUTSIDE, Orientation.VERTICAL, THIN_WALL_THICKNESS, WALL_VERTICAL_LENGTH_2))
    # WALL_LONGITUDE_2
    walls.append(Wall(WALL_LONGITUDE_2_INNER, WALL_LATITUDE_4, Orientation.VERTICAL, THIN_WALL_THICKNESS, WALL_VERTICAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_2_INNER, WALL_LATITUDE_6_OUTSIDE, Orientation.VERTICAL, THIN_WALL_THICKNESS, WALL_VERTICAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_2_OUTER, WALL_LATITUDE_8, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_VERTICAL_LENGTH_4))
    # WALL_LONGITUDE_3
    walls.append(Wall(WALL_LONGITUDE_3, WALL_LATITUDE_3, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_4))
    walls.append(Wall(WALL_LONGITUDE_3, WALL_LATITUDE_6_OUTSIDE, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_VERTICAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_3, WALL_LATITUDE_9, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    # WALL_LONGITUDE_4
    walls.append(Wall(WALL_LONGITUDE_4, WALL_LATITUDE_5_INSIDE, Orientation.VERTICAL, THIN_WALL_THICKNESS, WALL_LATITUDE_6_INSIDE+THIN_WALL_THICKNESS-WALL_LATITUDE_5_INSIDE))
    # WALL_LONGITUDE_5
    walls.append(Wall(WALL_LONGITUDE_5, WALL_LATITUDE_1, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_5, WALL_LATITUDE_3, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_5, WALL_LATITUDE_7_INSIDE, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_5, WALL_LATITUDE_9, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    # WALL_LONGITUDE_6
    walls.append(Wall(WALL_LONGITUDE_6, WALL_LATITUDE_5_INSIDE, Orientation.VERTICAL, THIN_WALL_THICKNESS, WALL_LATITUDE_6_INSIDE+THIN_WALL_THICKNESS-WALL_LATITUDE_5_INSIDE))
    # WALL_LONGITUDE_7
    walls.append(Wall(WALL_LONGITUDE_7, WALL_LATITUDE_3, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_4))
    walls.append(Wall(WALL_LONGITUDE_7, WALL_LATITUDE_6_OUTSIDE, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_VERTICAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_7, WALL_LATITUDE_9, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_HORIZONTAL_LENGTH_3))
    # WALL_LONGITUDE_8
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_4, Orientation.VERTICAL, THIN_WALL_THICKNESS, WALL_VERTICAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_6_OUTSIDE, Orientation.VERTICAL, THIN_WALL_THICKNESS, WALL_VERTICAL_LENGTH_3))
    walls.append(Wall(WALL_LONGITUDE_8, WALL_LATITUDE_8, Orientation.VERTICAL, MEDIUM_WALL_THICKNESS, WALL_VERTICAL_LENGTH_4))
    # WALL_LONGITUDE_9
    walls.append(Wall(WALL_LONGITUDE_9, WALL_LATITUDE_1, Orientation.VERTICAL, THIN_WALL_THICKNESS, WALL_VERTICAL_LENGTH_1))
    walls.append(Wall(WALL_LONGITUDE_9, WALL_LATITUDE_7_OUTSIDE, Orientation.VERTICAL, THIN_WALL_THICKNESS, WALL_VERTICAL_LENGTH_2))
    return walls

def add_point(points, x, y):
    point = Point(x, y)
    for wall in public_vars.walls:
        if point.overlaps_something(wall):
            return
    for super_point in public_vars.super_points:
        if point.collides(super_point):
            return
    points.append(point)

def generate_points():
    points = []
    for y in range(int(LANE_HORIZONTAL_1_LATTITUDE), int(LANE_HORIZONTAL_10_LATTITUDE+1), int(LANE_SIZE//2)):
        if y > LANE_HORIZONTAL_3_LATTITUDE and y < LANE_HORIZONTAL_7_LATTITUDE:
            continue
        for x in range(int(LANE_VERTICAL_1_LONGITUDE), int(LANE_VERTICAL_10_LONGITUDE+1), int(LANE_SIZE//2)):
            add_point(points, x, y)
    for y in range(int(LANE_HORIZONTAL_3_LATTITUDE+LANE_SIZE//2), int(LANE_HORIZONTAL_7_LATTITUDE-1), int(LANE_SIZE//2)):
        add_point(points, LANE_VERTICAL_3_LONGITUDE, y)
        add_point(points, LANE_VERTICAL_8_LONGITUDE, y)
    return points

def initialize_single_game_data():
    public_vars.pacman = Pacman(LANE_VERTICAL_5_5_LONGITUDE, LANE_HORIZONTAL_6_LATTITUDE, constants.Direction.LEFT, constants.YELLOW, False)
    public_vars.red_ghost = Ghost("red", LANE_VERTICAL_5_5_LONGITUDE, LANE_HORIZONTAL_4_LATTITUDE, constants.Direction.UP, "resources/images/red.png", Ghost.destination_red)
    public_vars.green_ghost = Ghost("green", LANE_VERTICAL_5_5_LONGITUDE+LANE_SIZE, LANE_HORIZONTAL_5_LATTITUDE, constants.Direction.LEFT, "resources/images/green.png", Ghost.destination_green)
    public_vars.pink_ghost = Ghost("pink", LANE_VERTICAL_5_5_LONGITUDE-LANE_SIZE, LANE_HORIZONTAL_5_LATTITUDE, constants.Direction.RIGHT, "resources/images/pink.png", Ghost.destination_pink)
    public_vars.orange_ghost = Ghost("orange", LANE_VERTICAL_5_5_LONGITUDE, LANE_HORIZONTAL_5_LATTITUDE, constants.Direction.UP, "resources/images/orange.png", Ghost.destination_orange)
    public_vars.ghosts = [public_vars.red_ghost, public_vars.green_ghost, public_vars.pink_ghost, public_vars.orange_ghost]

    # Walls
    public_vars.walls = generate_walls()

    # Super points
    public_vars.super_points = []
    public_vars.super_points.append(SuperPoint(LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_2_LATTITUDE-LANE_SIZE/2))
    public_vars.super_points.append(SuperPoint(LANE_VERTICAL_10_LONGITUDE, LANE_HORIZONTAL_2_LATTITUDE-LANE_SIZE/2))
    public_vars.super_points.append(SuperPoint(LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_8_LATTITUDE))
    public_vars.super_points.append(SuperPoint(LANE_VERTICAL_10_LONGITUDE, LANE_HORIZONTAL_8_LATTITUDE))

    # Points
    public_vars.points = generate_points()

    # Score 
    public_vars.score = 0

def new_valid_fruit_location(objects: List[Collidable]) -> Tuple[float, float]:
    while True:
        coordinates = ValidCharacterLocations.random_valid_coordinates()
        obj = Collidable(coordinates[0], coordinates[1], constants.LANE_SIZE/2)
        collides = False
        for item in objects:
            if obj.collides(item):
                collides = True
        if not collides:
            return coordinates

def generate_fruit() -> List[Fruit]:
    current_objects = public_vars.p1_pacmen.copy()
    current_objects.extend(public_vars.p2_pacmen)
    fruit_location = new_valid_fruit_location(current_objects)
    strawberry = Fruit.fruit_factory(fruit_location[0], fruit_location[1], constants.SupportedFruit.STRAWBERRY)
    current_objects.append(strawberry)
    fruit_location = new_valid_fruit_location(current_objects)
    cherry = Fruit.fruit_factory(fruit_location[0], fruit_location[1], constants.SupportedFruit.CHERRY)
    current_objects.append(cherry)
    fruit_location = new_valid_fruit_location(current_objects)
    orange = Fruit.fruit_factory(fruit_location[0], fruit_location[1], constants.SupportedFruit.ORANGE)
    current_objects.append(orange)
    return [strawberry, cherry, orange]


def initialize_multi_game_data():
    # Walls
    public_vars.walls = generate_walls()

    # Pacmen
    public_vars.p1_scared = random.choice([True, False])
    public_vars.p1_pacmen = [Pacman(LANE_VERTICAL_5_5_LONGITUDE, LANE_HORIZONTAL_2_LATTITUDE, constants.Direction.LEFT, constants.RED, True)]
    public_vars.p2_pacmen = [Pacman(LANE_VERTICAL_5_5_LONGITUDE, LANE_HORIZONTAL_8_LATTITUDE, constants.Direction.RIGHT, constants.GREEN, True)]
    
    # Fruit
    public_vars.fruit = generate_fruit()
