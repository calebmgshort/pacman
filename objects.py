import pygame
import constants

class Object:
    def __init__(self, screen, x, width, y, height):
        self.screen = screen
        self.x = x
        self.width = width
        self.y = y
        self.height = height

    def overlapping_with_orientation(self, other, orientation):
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

    def overlapping(self, other):
        return self.overlapping_with_orientation(other, constants.Orientation.HORIZONTAL) and self.overlapping_with_orientation(other, constants.Orientation.VERTICAL)

class Wall(Object):
    def __init__(self, screen, left, top, orientation, length):
        width = 0
        height = 0
        if orientation == constants.Orientation.HORIZONTAL:
            width = length
            height = constants.WALL_THICKNESS
        elif orientation == constants.Orientation.VERTICAL:
            width = constants.WALL_THICKNESS
            height = length
        else:
            raise TypeError("The orientation provided is invalid")
        super(Wall, self).__init__(screen, left, width, top, height)
        self.object = pygame.Rect(left, top, width, height)

    def render(self):
        pygame.draw.rect(self.screen, constants.BLUE, self.object)

class Character(Object):
    def __init__(self, screen, x, y, direction, image_path):
        super(Character, self).__init__(screen, x, constants.CHARACTER_SIZE, y, constants.CHARACTER_SIZE)
        initial_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(initial_image, (constants.CHARACTER_SIZE,constants.CHARACTER_SIZE))
        self.direction = direction

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))
    
    def move(self, wall):
        old_x = self.x
        old_y = self.y
        if self.direction == constants.Direction.RIGHT:
            self.x += constants.CHARACTER_SPEED
        elif self.direction == constants.Direction.LEFT:
            self.x -= constants.CHARACTER_SPEED
        elif self.direction == constants.Direction.UP:
            self.y -= constants.CHARACTER_SPEED
        elif self.direction == constants.Direction.DOWN:
            self.y += constants.CHARACTER_SPEED
        # Handle the case where we've reached the edge of the screen
        if self.x < 0:
            self.x = 0
        if self.x > constants.SCREEN_WIDTH - constants.CHARACTER_SIZE:
            self.x = constants.SCREEN_WIDTH - constants.CHARACTER_SIZE
        if self.y < 0:
            self.y = 0
        if self.y > constants.SCREEN_HEIGHT - constants.CHARACTER_SIZE:
            self.y = constants.SCREEN_HEIGHT - constants.CHARACTER_SIZE
        # Handle the case where we've run into a wall
        if self.overlapping(wall):
            self.x = old_x
            self.y = old_y