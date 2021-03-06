import unittest
from objects import *
from constants import *
from init import generate_walls

class TestOverlappable(unittest.TestCase):

    def test_overlapping(self):
        # x, width, y, length
        basic = Overlappable(50, 50, 50, 50)
        obj_overlapping = Overlappable(99, 10, 99, 10)
        obj_not_overlapping = Overlappable(100, 50, 100, 50)
        obj_inside = Overlappable(60, 10, 60, 10)
        obj_outside = Overlappable(40, 70, 40, 70)
        self.assertTrue(basic.overlapping(obj_overlapping))
        self.assertTrue(obj_overlapping.overlapping(basic))
        self.assertFalse(basic.overlapping(obj_not_overlapping))
        self.assertFalse(obj_not_overlapping.overlapping(basic))
        self.assertTrue(basic.overlapping(obj_inside))
        self.assertTrue(obj_inside.overlapping(basic))
        self.assertTrue(basic.overlapping(obj_outside))
        self.assertTrue(obj_outside.overlapping(basic))

# class TestCollidable(unittest.TestCase):
#     def test_overlaps_something(self):
#         wall  =

class TestCharacter(unittest.TestCase):

    def test_basic_move(self):
        # x, y, direction
        char = Character(10, 10, Direction.RIGHT)
        self.assertEqual((char.x, char.y), (10, 10))
        char._basic_move(Direction.RIGHT, 0.1)
        self.assertEqual((char.x, char.y), (10.1, 10))
        char._basic_move(Direction.DOWN, 0.1)
        self.assertEqual((char.x, char.y), (10.1, 10.1))
        char._basic_move(Direction.UP, 0.2)
        self.assertEqual((char.x, char.y), (10.1, 9.9))
        char._basic_move(Direction.LEFT, 0.2)
        self.assertEqual((char.x, char.y), (9.9, 9.9))
    
    def test_move(self):
        char = Character(LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_1_LATTITUDE, Direction.RIGHT)
        self.assertEqual((char.x, char.y), (LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_1_LATTITUDE))
        # Check basic movement
        char.move()
        self.assertEqual((char.x, char.y), (LANE_VERTICAL_1_LONGITUDE + CHARACTER_SPEED, LANE_HORIZONTAL_1_LATTITUDE))
        # Check that we won't move if we butt into a wall
        char.x = LANE_VERTICAL_5_LONGITUDE - CHARACTER_SPEED/2
        char.move()
        self.assertEqual((char.x, char.y), (LANE_VERTICAL_5_LONGITUDE - CHARACTER_SPEED/2, LANE_HORIZONTAL_1_LATTITUDE))
        # Check that we will change directions if there is nothing blocking us
        char.x, char.y, char.direction, char.desired_direction = LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_1_LATTITUDE, Direction.RIGHT, Direction.DOWN
        char.move()
        self.assertEqual(char.direction, Direction.DOWN)
        self.assertEqual(char.desired_direction, Direction.DOWN)
        self.assertEqual((char.x, char.y), (LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_1_LATTITUDE + CHARACTER_SPEED))
        # Check that we won't change directions if there is something blocking us
        char.desired_direction = Direction.RIGHT
        char.move()
        self.assertEqual(char.direction, Direction.DOWN)
        self.assertEqual(char.desired_direction, Direction.RIGHT)
        self.assertEqual((char.x, char.y), (LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_1_LATTITUDE + 2*CHARACTER_SPEED))

        # Additional checks to help me debug this
        char.x, char.y, char.direction, char.desired_direction = LANE_VERTICAL_4_LONGITUDE, LANE_HORIZONTAL_6_LATTITUDE, Direction.LEFT, Direction.DOWN
        char.move()
        self.assertEqual(char.desired_direction, Direction.DOWN)
        self.assertEqual(char.direction, Direction.DOWN)
        self.assertEqual((char.x, char.y), (LANE_VERTICAL_4_LONGITUDE, LANE_HORIZONTAL_6_LATTITUDE + CHARACTER_SPEED))
    
class TestGhost(unittest.TestCase):

    def test_in_center(self):
        green = Ghost("green", constants.SCREEN_WIDTH//2+constants.LANE_SIZE//2, constants.SCREEN_HEIGHT//2-constants.LANE_SIZE//2, constants.Direction.LEFT, "resources/images/green.png", lambda: (0,constants.SCREEN_HEIGHT))
        self.assertTrue(green.in_center())
        green.x = 50
        green.y = 50
        self.assertFalse(green.in_center())

    def test_dead_end(self):
        green = Ghost("green", constants.LANE_VERTICAL_1_LONGITUDE, constants.LANE_HORIZONTAL_1_LATTITUDE, constants.Direction.LEFT, "resources/images/green.png", lambda: (0,constants.SCREEN_HEIGHT))
        self.assertTrue(green._dead_end())
        green.x += 0.1
        self.assertFalse(green._dead_end())
    
    def test_on_intersection(self):
        red = Ghost("red", constants.LANE_VERTICAL_1_LONGITUDE, constants.LANE_HORIZONTAL_2_LATTITUDE, constants.Direction.DOWN, "resources/images/red.png", lambda: (0,0))
        self.assertTrue(red._on_intersection())
        
    def test_choose_direction(self):
        # Upper left corner, moving up. Should go right
        green = Ghost("green", constants.LANE_VERTICAL_1_LONGITUDE, constants.LANE_HORIZONTAL_1_LATTITUDE, constants.Direction.UP, "resources/images/green.png", lambda: (0,constants.SCREEN_HEIGHT))
        self.assertEqual(constants.Direction.UP, green.desired_direction)
        green._choose_direction(green.choose_destination())
        self.assertEqual(constants.Direction.RIGHT, green.desired_direction)
        # In center, at intersection. Should choose to go up
        green.x, green.y = constants.LANE_VERTICAL_5_5_LONGITUDE, constants.LANE_HORIZONTAL_5_LATTITUDE
        green.direction, green.desired_direction = constants.Direction.LEFT, constants.Direction.LEFT
        green._choose_direction(green.choose_destination())
        self.assertEqual(constants.Direction.UP, green.desired_direction)
        # Just after getting out of the center. Should go left
        green.y = constants.LANE_HORIZONTAL_4_LATTITUDE
        green.direction, green.desired_direction = constants.Direction.UP, constants.Direction.UP
        green._choose_direction(green.choose_destination())
        self.assertEqual(constants.Direction.LEFT, green.desired_direction)
        # In the upper left corner, down one spot. heading down. Should go right
        red = Ghost("red", constants.LANE_VERTICAL_1_LONGITUDE, constants.LANE_HORIZONTAL_2_LATTITUDE, constants.Direction.DOWN, "resources/images/red.png", lambda: (0,0))
        self.assertTrue(red._on_intersection())
        self.assertEqual(constants.Direction.DOWN, red.desired_direction)
        red._choose_direction(red.choose_destination())
        self.assertEqual(constants.Direction.RIGHT, red.desired_direction)
        red_x, red_y = red.x, red.y
        red.move()
        self.assertEqual(red.direction, Direction.RIGHT)
        self.assertEqual([red_x+CHARACTER_SPEED, red_y], [red.x, red_y])
        # In a dead end in the center. Should go backwards
        green.x, green.y = LANE_VERTICAL_5_LONGITUDE-THIN_WALL_THICKNESS, constants.LANE_HORIZONTAL_5_LATTITUDE
        green.direction, green.desired_direction = constants.Direction.LEFT, constants.Direction.LEFT
        green._choose_direction(green.choose_destination())
        self.assertEqual(constants.Direction.RIGHT, green.desired_direction)

if __name__ == '__main__':
    unittest.main()