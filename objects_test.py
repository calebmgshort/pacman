import unittest
from objects import *
from constants import *
from init import generate_walls

class TestObject(unittest.TestCase):

    def test_overlapping(self):
        # x, width, y, length
        basic = Object(50, 50, 50, 50)
        obj_overlapping = Object(99, 10, 99, 10)
        obj_not_overlapping = Object(100, 50, 100, 50)
        obj_inside = Object(60, 10, 60, 10)
        obj_outside = Object(40, 70, 40, 70)
        self.assertTrue(basic.overlapping(obj_overlapping))
        self.assertTrue(obj_overlapping.overlapping(basic))
        self.assertFalse(basic.overlapping(obj_not_overlapping))
        self.assertFalse(obj_not_overlapping.overlapping(basic))
        self.assertTrue(basic.overlapping(obj_inside))
        self.assertTrue(obj_inside.overlapping(basic))
        self.assertTrue(basic.overlapping(obj_outside))
        self.assertTrue(obj_outside.overlapping(basic))

        self.assertTrue(basic.overlapping_list([obj_overlapping, obj_not_overlapping, obj_inside, obj_outside]))
        self.assertTrue(basic.overlapping_list([obj_not_overlapping, obj_overlapping]))
        self.assertFalse(basic.overlapping_list([obj_not_overlapping]))
        

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
        public_vars.walls = []

        char = Character(100, 100, Direction.RIGHT)
        self.assertEqual((char.x, char.y), (100, 100))
        # Check basic movement
        char.move()
        self.assertEqual((char.x, char.y), (100 + CHARACTER_SPEED, 100))
        # Check that we'll move if we don't butt into a wall
        public_vars.walls.append(Wall(100 + CHARACTER_SIZE + 2.5 * CHARACTER_SPEED, 100, Orientation.VERTICAL, 10, 100))
        char.move()
        self.assertEqual((char.x, char.y), (100 + CHARACTER_SPEED*2, 100))
        # Check that we won't move if we do butt into a wall
        char.move()
        self.assertEqual((char.x, char.y), (100 + CHARACTER_SPEED*2, 100))
        # Check that we will change directions if there is nothing blocking us
        char.desired_direction = Direction.DOWN
        char.move()
        self.assertEqual((char.x, char.y), (100 + CHARACTER_SPEED*2, 100 + CHARACTER_SPEED))
        self.assertEqual(char.direction, Direction.DOWN)
        self.assertEqual(char.desired_direction, Direction.DOWN)
        # Check that we won't change directions if there is something blocking us
        char.desired_direction = Direction.RIGHT
        char.move()
        self.assertEqual((char.x, char.y), (100 + CHARACTER_SPEED*2, 100 + CHARACTER_SPEED*2))
        self.assertEqual(char.direction, Direction.DOWN)
        self.assertEqual(char.desired_direction, Direction.RIGHT)
        # Check that we won't switch direction even if we can move in that direction. We have to be able to move a full body in that direction
        char.x = 100 - (LANE_SIZE - CHARACTER_SIZE)
        char.y = 100
        char.move()
        self.assertEqual((char.x, char.y), (100 - (LANE_SIZE - CHARACTER_SIZE), 100 + CHARACTER_SPEED))
        self.assertEqual(char.direction, Direction.DOWN)
        self.assertEqual(char.desired_direction, Direction.RIGHT)
    
class TestGhost(unittest.TestCase):

    def setUp(self):
        public_vars.walls = []

    # TODO: Test __in_center
    def test_in_center(self):
        green = Ghost("green", constants.SCREEN_WIDTH//2+constants.CHARACTER_SIZE//2, constants.SCREEN_HEIGHT//2-constants.CHARACTER_SIZE//2, constants.Direction.LEFT, "resources/green.png", lambda: (0,constants.SCREEN_HEIGHT))
        self.assertTrue(green._in_center())
        green.x = 50
        green.y = 50
        self.assertFalse(green._in_center())

    def test_dead_end(self):
        green = Ghost("green", 0, 0, constants.Direction.RIGHT, "resources/green.png", lambda: (0,constants.SCREEN_HEIGHT))
        public_vars.walls.append(Wall(constants.CHARACTER_SIZE + constants.CHARACTER_SPEED, 0, Orientation.VERTICAL, 10, 100))
        self.assertFalse(green._dead_end())
        green.x += 0.1
        self.assertTrue(green._dead_end())
    def test_on_intersection(self):
        public_vars.walls = generate_walls()
        # Upper left corner. Not an intersection
        green = Ghost("green", constants.LANE_VERTICAL_1_LONGITUDE-CHARACTER_SIZE/2, constants.LANE_HORIZONTAL_1_LATTITUDE-CHARACTER_SIZE/2, constants.Direction.UP, "resources/green.png", lambda: (0,constants.SCREEN_HEIGHT))
        self.assertFalse(green._on_intersection())
        # In the middle. Yes an intersection
        green.x, green.y = constants.SCREEN_WIDTH//2-constants.CHARACTER_SIZE//2, constants.SCREEN_HEIGHT//2-constants.CHARACTER_SIZE//2
        self.assertTrue(green._on_intersection())
        # In the middle but 1 lane up. Yes an intersection
        green.y = constants.LANE_HORIZONTAL_4_LATTITUDE - CHARACTER_SIZE//2
        self.assertTrue(green._on_intersection())
        # Between the middle and upper-middle lanes. Not an intersection
        green.y = constants.LANE_HORIZONTAL_4_LATTITUDE
        self.assertFalse(green._on_intersection())
        
    def test_choose_direction(self):
        public_vars.walls = generate_walls()
        # Upper left corner, moving up. Should go right
        green = Ghost("green", constants.LANE_VERTICAL_1_LONGITUDE-CHARACTER_SIZE/2, constants.LANE_HORIZONTAL_1_LATTITUDE-CHARACTER_SIZE/2, constants.Direction.UP, "resources/green.png", lambda: (0,constants.SCREEN_HEIGHT))
        self.assertEqual(constants.Direction.UP, green.desired_direction)
        green._choose_direction(green.choose_destination())
        self.assertEqual(constants.Direction.RIGHT, green.desired_direction)
        # In center, at intersection. Should choose to go up
        green.x, green.y = constants.SCREEN_WIDTH//2-constants.CHARACTER_SIZE//2, constants.SCREEN_HEIGHT//2-constants.CHARACTER_SIZE//2
        green.direction, green.desired_direction = constants.Direction.LEFT, constants.Direction.LEFT
        green._choose_direction(green.choose_destination())
        self.assertEqual(constants.Direction.UP, green.desired_direction)
        # Just after getting out of the center. Should go left
        green.y = constants.LANE_HORIZONTAL_4_LATTITUDE - CHARACTER_SIZE//2
        green.direction, green.desired_direction = constants.Direction.UP, constants.Direction.UP
        green._choose_direction(green.choose_destination())
        self.assertEqual(constants.Direction.LEFT, green.desired_direction)
        # In a dead end in the center. Should go backwards
        # green.x, green.y = constants.WALL_LONGITUDE_4+constants.THIN_WALL_THICKNESS, constants.SCREEN_HEIGHT//2-constants.CHARACTER_SIZE//2
        # green.direction, green.desired_direction = constants.Direction.LEFT, constants.Direction.LEFT
        # green._choose_direction(green.choose_destination())
        # self.assertEqual(constants.Direction.RIGHT, green.desired_direction)
        
    # TODO: Test _choose_direction
    # TODO: Test move



if __name__ == '__main__':
    unittest.main()