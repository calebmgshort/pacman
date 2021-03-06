import pygame
import pygame.gfxdraw
import constants
import util
import public_vars
import abc
import math
import time
from valid_character_locations import ValidCharacterLocations
from typing import Tuple
from enum import Enum
from random import random


class Overlappable:
    def __init__(self, x: float, width: float, y: float, height: float):
        self.x = x
        self.width = width
        self.y = y
        self.height = height
    
    def __overlapping_with_orientation(self, other: 'Overlappable', orientation: constants.Direction) -> bool:
        self_begin, self_end, other_begin, other_end = 0,0,0,0
        if orientation == constants.Orientation.HORIZONTAL:
            self_begin = self.x
            self_end = self.x + self.width
            other_begin = other.x
            other_end = other.x + other.width
        elif orientation == constants.Orientation.VERTICAL:
            self_begin = self.y
            self_end = self.y + self.height
            other_begin = other.y
            other_end = other.y + other.height
        else:
            raise TypeError("The orientation type is not valid!")

        # This's edge is within other's frame
        if (self_begin < other_end and self_begin > other_begin) or (self_end < other_end and self_end > other_begin):
            return True
        # Other's edge is within this's frame
        if (other_begin < self_end and other_begin > self_begin) or (other_end < self_end and other_end > self_begin):
            return True
        return False

    def overlapping(self, other: 'Overlappable') -> bool:
        return self.__overlapping_with_orientation(other, constants.Orientation.HORIZONTAL) and self.__overlapping_with_orientation(other, constants.Orientation.VERTICAL)

class Wall(Overlappable):
    def __init__(self, left: float, top: float, orientation: float, thickness: float, length: float):
        width = 0
        height = 0
        if orientation == constants.Orientation.HORIZONTAL:
            width = length
            height = thickness
        elif orientation == constants.Orientation.VERTICAL:
            width = thickness
            height = length
        else:
            raise ValueError("The direction is not a valid enum value")
        super().__init__(left, width, top, height)
        self.object = pygame.Rect(left, top, width, height)

    def render(self):
        pygame.draw.rect(public_vars.screen, constants.BLUE, self.object)


class Collidable():
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.radius = radius
        self.overlappable = Overlappable(x-radius, radius*2, y-radius, radius*2)

    def collides(self, other: 'Collidable') -> bool:
        return util.distance((self.x, self.y), (other.x, other.y)) < self.radius + other.radius
    
    def overlaps_something(self, other: Overlappable) -> bool:
        return self.overlappable.overlapping(other)

class Fruit(Collidable):
    @staticmethod
    def fruit_factory(x: float, y: float, fruit_type: constants.SupportedFruit):
        if fruit_type == constants.SupportedFruit.STRAWBERRY:
            image_path = "resources/images/strawberry.png"
        elif fruit_type == constants.SupportedFruit.CHERRY:
            image_path = "resources/images/cherry.png"
        elif fruit_type == constants.SupportedFruit.ORANGE:
            image_path = "resources/images/orange_fruit.png"
        else:
            raise ValueError("The provided fruit type is not supported")
        return Fruit(x, y, fruit_type, image_path)

    def __init__(self, x: float, y: float, fruit_type: constants.SupportedFruit, image_path: str):
        if not ValidCharacterLocations.valid_coordinates((x,y)):
            raise ValueError("The coordinates for this Fruit object are invalid")
        super().__init__(x, y, constants.LANE_SIZE/2)
        self.fruit_type = fruit_type
        self.image = pygame.transform.scale(pygame.image.load(image_path), (round(constants.LANE_SIZE), round(constants.LANE_SIZE)))

    def render(self):
        public_vars.screen.blit(self.image, (self.x-constants.LANE_SIZE/2, self.y-constants.LANE_SIZE/2))
        

class Circle(Collidable):
    def __init__(self, x: float, y: float, radius: float, color: Tuple[int, int, int]):
        super().__init__(x, y, radius)
        self.color = color
    
    def render(self):
        pygame.draw.circle(public_vars.screen, self.color, (self.x, self.y), self.radius)


class Point(Circle):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, 4, constants.LIGHT_PINK)

class SuperPoint(Circle):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, 8, constants.LIGHT_PINK)

class Character(Collidable):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, x: float, y: float, direction: constants.Direction):
        Collidable.__init__(self, x, y, constants.LANE_SIZE/2)
        self.direction = direction
        self.desired_direction = direction
    
    def _basic_move(self, direction: float, diplacement: float):
        if direction == constants.Direction.RIGHT:
            self.x += diplacement
        elif direction == constants.Direction.LEFT:
            self.x -= diplacement
        elif direction == constants.Direction.UP:
            self.y -= diplacement
        elif direction == constants.Direction.DOWN:
            self.y += diplacement
        else:
            raise ValueError("The direction is not a valid enum value")
        # In case by some minor python arithmetic error we're on a weird location, round our location
        self.x, self.y = round(self.x, 1), round(self.y, 1)
    
    def _in_valid_position(self):
        return ValidCharacterLocations.valid_coordinates((self.x, self.y))

    def move(self):
        if not self._in_valid_position():
            raise Exception("Move (beginning): called with character in invalid location")
        # Change the direction to be the desired direction if the desired direction is a valid option
        stored_x, stored_y = self.x, self.y
        self._basic_move(self.desired_direction, constants.LANE_SIZE)
        if self._in_valid_position():
            self.direction = self.desired_direction
        self.x, self.y = stored_x, stored_y
        # Make the most basic move
        self._basic_move(self.direction, constants.CHARACTER_SPEED)
        # Handle the case where we've reached the edge of the map
        if self.y == constants.LANE_HORIZONTAL_5_LATTITUDE:
            if self.x < constants.LANE_VERTICAL_1_LONGITUDE - constants.THIN_WALL_THICKNESS:
                self.x = constants.LANE_VERTICAL_10_LONGITUDE - constants.THIN_WALL_THICKNESS
            elif self.x > constants.LANE_VERTICAL_10_LONGITUDE + constants.THIN_WALL_THICKNESS:
                self.x = constants.LANE_VERTICAL_1_LONGITUDE - constants.THIN_WALL_THICKNESS
        # Handle the case where we've run into a wall
        if not self._in_valid_position():
            self.x, self.y = stored_x, stored_y
        if not self._in_valid_position():
            raise Exception("Move (end): character in invalid location")

class Ghost(Character):

    class GhostMode(Enum):
        NORMAL = 0
        SCARED = 1
        RESPAWN = 2

    class GhostSubmode(Enum):
        NORMAL = 0
        ABOUT_TO_SWITCH = 1

    def __init__(self, name: str, x: float, y: float, direction: constants.Direction, image_path: str, choose_destination):
        super().__init__(x, y, direction)
        self.name = name
        self.normal_image = pygame.transform.scale(pygame.image.load(image_path), (round(constants.LANE_SIZE), round(constants.LANE_SIZE)))
        self.scared_image = pygame.transform.scale(pygame.image.load("resources/images/scared.png"), (round(constants.LANE_SIZE), round(constants.LANE_SIZE)))
        self.scared_changing_image = pygame.transform.scale(pygame.image.load("resources/images/scared_changing.png"), (round(constants.LANE_SIZE), round(constants.LANE_SIZE)))
        self.respawn_image = pygame.transform.scale(pygame.image.load("resources/images/respawn.png"), (round(constants.LANE_SIZE), round(constants.LANE_SIZE/2)))
        self.choose_destination = choose_destination
        self.previously_on_intersection = False
        self.mode = Ghost.GhostMode.NORMAL
        self.submode = Ghost.GhostSubmode.NORMAL

    def set_submode(self, submode: "Ghost.GhostSubmode"):
        if self.mode == Ghost.GhostMode.SCARED:
            if submode != Ghost.GhostSubmode.ABOUT_TO_SWITCH and submode != Ghost.GhostSubmode.NORMAL:
                raise ValueError("Ghost submode invalid")
            self.submode = submode
            return
        raise ValueError("Ghost submode can not be set within a ghost mode other than Scared")

    def render(self):
        if self.mode == Ghost.GhostMode.SCARED:
            if self.submode == Ghost.GhostSubmode.NORMAL:
                public_vars.screen.blit(self.scared_image, (self.x-constants.LANE_SIZE/2, self.y-constants.LANE_SIZE/2))
            elif self.submode == Ghost.GhostSubmode.ABOUT_TO_SWITCH:
                current_time = time.time()
                time_dif = current_time - public_vars.render_start_time
                time_dif %= 1
                if time_dif < 0.5:
                    public_vars.screen.blit(self.scared_image, (self.x-constants.LANE_SIZE/2, self.y-constants.LANE_SIZE/2))
                else: 
                    public_vars.screen.blit(self.scared_changing_image, (self.x-constants.LANE_SIZE/2, self.y-constants.LANE_SIZE/2))
                pass
            else:
                raise ValueError("Ghost submode not valid")
        elif self.mode == Ghost.GhostMode.RESPAWN:
            public_vars.screen.blit(self.respawn_image, (self.x-constants.LANE_SIZE/2, self.y-constants.LANE_SIZE/2))
        else:
            public_vars.screen.blit(self.normal_image, (self.x-constants.LANE_SIZE/2, self.y-constants.LANE_SIZE/2))
    
    def move(self):
        if self._on_intersection():
            pacman = None
            if public_vars.game_mode == constants.GameMode.SINGLE_PLAY:
                pacman = public_vars.pacman
            elif public_vars.game_mode == constants.GameMode.MULTI_PLAY:
                # If we're pursuing, we should always pursue the scared pacman!
                if self.mode != Ghost.GhostMode.SCARED:
                    if public_vars.p1_scared:
                        pacman = public_vars.p1_pacmen[0]
                    else:
                        pacman = public_vars.p2_pacmen[0]
                # If we're scared, we should always run away from the pursuing pacman!
                else:
                    if public_vars.p1_scared:
                        pacman = public_vars.p2_pacmen[0]
                    else:
                        pacman = public_vars.p1_pacmen[0]
            else:
                raise ValueError("ghost move: the game mode is not a play mode")
            if self.mode == Ghost.GhostMode.NORMAL:
                destination = self.choose_destination(pacman)
            elif self.mode == Ghost.GhostMode.SCARED:
                destination = Ghost.destination_run_away(pacman, self)
            elif self.mode == Ghost.GhostMode.RESPAWN:
                destination = Ghost.destination_respawn()
            else:
                raise ValueError("Ghost mode is not valid")
            self._choose_direction(destination)
        else:
            if self._dead_end():
                if self._on_intersection():
                    raise ValueError("Wasn't expecting on_intersection to be true here")
                self._choose_direction(None)
        super().move()
    
    def _on_intersection(self) -> bool:
        return ValidCharacterLocations.on_intersection((self.x, self.y))
    
    def _dead_end(self) -> bool:
        self._basic_move(self.direction, 0.1)
        dead_end = True
        if self._in_valid_position():
            dead_end = False
        elif self.y == constants.LANE_HORIZONTAL_5_LATTITUDE and (
            self.x < constants.LANE_VERTICAL_1_LONGITUDE - constants.THIN_WALL_THICKNESS or self.x > constants.LANE_VERTICAL_10_LONGITUDE + constants.THIN_WALL_THICKNESS):
            dead_end = False
        self._basic_move(util.opposite_direction(self.direction), 0.1)
        return dead_end
    
    def _choose_direction(self, destination):
        valid_directions = [constants.Direction.LEFT, constants.Direction.RIGHT, constants.Direction.UP, constants.Direction.DOWN]
        old_x, old_y = self.x, self.y
        valid_directions.remove(util.opposite_direction(self.direction))
        for direction in valid_directions[:]:
            self._basic_move(direction, constants.LANE_SIZE)
            if not self._in_valid_position():
                valid_directions.remove(direction)
            self.x, self.y = old_x, old_y
        if len(valid_directions) == 1:
            self.desired_direction = valid_directions.pop()
        elif len(valid_directions) > 1:
            if self.in_center():
                self.desired_direction = constants.Direction.UP
                return
            best_distance = constants.SCREEN_WIDTH + constants.SCREEN_HEIGHT
            best_direction = None
            for direction in valid_directions:
                self._basic_move(direction, constants.CHARACTER_SPEED)
                distance = 0
                try:
                    distance = util.distance((self.x, self.y), destination)
                except TypeError:
                    print("Name: {}, Pos: ({},{}), in_center: {}, _on_intersection: {}".format(self.name, self.x, self.y, self.in_center(), self._on_intersection()))
                    raise TypeError("Distance called with invalid value")
                if distance < best_distance:
                    best_distance = distance
                    best_direction = direction
                self.x, self.y = old_x, old_y
            self.desired_direction = best_direction
        else:
            self.desired_direction = util.opposite_direction(self.direction)
    
    def in_center(self) -> bool:
        return (self.x > constants.WALL_LONGITUDE_4 and self.x < constants.WALL_LONGITUDE_6) and (
            self.y > constants.WALL_LATITUDE_5_INSIDE and self.y < constants.WALL_LATITUDE_6_INSIDE)

    # When running away, just move in the opposite direction of pacman
    @staticmethod
    def destination_run_away(pacman: 'Pacman', myself: 'Ghost'):
        x_dif = pacman.x - myself.x
        y_dif = pacman.y - myself.y
        return (pacman.x - 2*x_dif, pacman.y - y_dif)
    
    # When respawning, head for the center
    @staticmethod
    def destination_respawn():
        return (constants.LANE_VERTICAL_5_5_LONGITUDE, constants.LANE_HORIZONTAL_5_LATTITUDE)
    
    # Red hunts. Goes straight for pacman
    @staticmethod
    def destination_red(pacman: 'Pacman'):
        return (pacman.x, pacman.y)

    # Pink ambushes. Goes 4 lanes in head of pacman
    @staticmethod
    def destination_pink(pacman: 'Pacman'):
        if pacman.direction == constants.Direction.RIGHT:
            return (pacman.x + 4 * constants.LANE_SIZE, pacman.y)
        elif pacman.direction == constants.Direction.LEFT:
            return (pacman.x - 4 * constants.LANE_SIZE, pacman.y)
        elif pacman.direction == constants.Direction.UP:
            return (pacman.x, pacman.y - 4*constants.LANE_SIZE)
        elif pacman.direction == constants.Direction.DOWN:
            return (pacman.x, pacman.y + 4*constants.LANE_SIZE)
        else:
            raise ValueError("The direction provided is not valid")
        raise ValueError("This statement should never be reached! And the direction provided is not valid")

    # Green goes to the point accross pacman from red
    @staticmethod
    def destination_green(pacman: 'Pacman'):
        x_dif = pacman.x - public_vars.red_ghost.x
        y_dif = pacman.y - public_vars.red_ghost.y
        return (pacman.x + x_dif, pacman.y + y_dif)

    # Orange hunts like red, unless it's too close, in which case it picks a random spot. 
    @staticmethod
    def destination_orange(pacman: 'Pacman'):
        if util.distance((public_vars.orange_ghost.x, public_vars.orange_ghost.y), (pacman.x, pacman.y)) > 4 * constants.LANE_SIZE * math.sqrt(2):
            return Ghost.destination_red(pacman)
        return (random() * constants.SCREEN_WIDTH, random() * constants.SCREEN_HEIGHT)

def draw_pacman_mouth(center_x: float, center_y: float, max_angle: float, direction: constants.Direction):
    # Calculate current angle.
    angle = 0

    current_time = time.time()
    time_dif = current_time - public_vars.render_start_time
    time_dif %= 1
    if time_dif - 0.5 < 0:
        angle = max_angle - max_angle*time_dif*2
    else: 
        angle = max_angle * (time_dif - 0.5) * 2
    angle = int(angle)
    extra = angle % 5
    angle -= extra
    
    # round to nearest 5
    # I have angle, adjacent
    # tan(angle) = opposite / adjacent

    # adjacent = constants.LANE_SIZE//2
    # opposite = math.tan(angle/2) * adjacent
    hypotenuse = constants.LANE_SIZE/2
    adjacent = abs(math.cos(angle/2)) * hypotenuse
    opposite = abs(math.sin(angle/2)) * hypotenuse

    rec_width = hypotenuse - adjacent + 1
    rec_length = constants.LANE_SIZE

    if direction == constants.Direction.RIGHT:
        pygame.draw.polygon(public_vars.screen, constants.BLACK, [(center_x, center_y), (center_x+adjacent, center_y + opposite), (center_x+adjacent, center_y-opposite)])
        pygame.draw.rect(public_vars.screen, constants.BLACK, pygame.Rect(center_x + adjacent, center_y - opposite, rec_width, rec_length))
    elif direction == constants.Direction.LEFT:
        pygame.draw.polygon(public_vars.screen, constants.BLACK, [(center_x, center_y), (center_x-adjacent, center_y + opposite), (center_x-adjacent, center_y-opposite)])
        pygame.draw.rect(public_vars.screen, constants.BLACK, pygame.Rect(center_x - hypotenuse, center_y - hypotenuse, rec_width, rec_length))
    elif direction == constants.Direction.UP:
        pygame.draw.polygon(public_vars.screen, constants.BLACK, [(center_x, center_y), (center_x-opposite, center_y-adjacent), (center_x+opposite, center_y-adjacent)])  
        pygame.draw.rect(public_vars.screen, constants.BLACK, pygame.Rect(center_x - hypotenuse, center_y - hypotenuse, rec_length, rec_width))
    elif direction == constants.Direction.DOWN:
        pygame.draw.polygon(public_vars.screen, constants.BLACK, [(center_x, center_y), (center_x-opposite, center_y+adjacent), (center_x+opposite, center_y+adjacent)])
        pygame.draw.rect(public_vars.screen, constants.BLACK, pygame.Rect(center_x - hypotenuse, center_y + adjacent, rec_length, rec_width))   
    else:
        raise ValueError("Direction not valid")

class Pacman(Character, Circle):

    def duplicate_opposite(self) -> 'Pacman':
        return Pacman(self.x, self.y, util.opposite_direction(self.direction), self.color, self.multiplayer)

    def __init__(self, x: float, y: float, direction: constants.Direction, color: Tuple[int, int, int], multiplayer: bool):
        Character.__init__(self, x, y, direction)
        self.color = color
        self.multiplayer = multiplayer
    
    def render(self, scared):
        color = self.color
        if self.multiplayer and scared:
            color = constants.DODGERBLUE
        pygame.draw.circle(public_vars.screen, color, (self.x, self.y), constants.LANE_SIZE/2)
        draw_pacman_mouth(self.x, self.y, 30, self.direction)
        