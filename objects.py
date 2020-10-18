import pygame
import constants

class Object:
    def __init__(self, screen, left, right, top, bottom):
        self.screen = screen
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

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
        super(Wall, self).__init__(screen, left, left + width, top, top + length)
        self.object = pygame.Rect(left, top, width, height)

    def render(self):
        pygame.draw.rect(self.screen, constants.BLUE, self.object)
