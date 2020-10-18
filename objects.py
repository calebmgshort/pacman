import pygame
import constants

class Object:
    def __init__(self, screen, x, width, y, height):
        self.screen = screen
        self.x = x
        self.width = width
        self.y = y
        self.height = height

    def overlapping_horizontal(self, other):
        self_left = self.x
        self_right = self.x + self.width
        other_left = other.x
        other_right = other.x + other.width

        # This's edge is within other's frame
        if (self_left < other_right and self_left > other_left) or (self_right < other_right and self_right > other_left):
            return True
        # Other's edge is within this's frame
        if (other_left < self_right and other_left > self_left) or (other_right < self_right and other_right > self_left):
            return True
        return False

    def overlapping_vertical(self, other):
        self_top = self.y
        self_bottom = self.y + self.height
        other_top = other.y
        other_bottom = other.y + other.height

        # This's edge is within other's frame
        if (self_top < other_bottom and self_top > other_top) or (self_bottom < other_bottom and self_bottom > other_top):
            return True
        # Other's edge is within this's frame
        if (other_top < self_bottom and other_top > self_top) or (other_bottom < self_bottom and other_bottom > self_top):
            return True
        return False

    def overlapping(self, other):
        return self.overlapping_horizontal(other) and self.overlapping_vertical(other)

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