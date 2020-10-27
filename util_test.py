import unittest
from util import *
from constants import Direction

class TestUtil(unittest.TestCase):

    def test_opposite_direction(self):
        self.assertEqual(opposite_direction(Direction.UP), Direction.DOWN)
        self.assertEqual(opposite_direction(Direction.DOWN), Direction.UP)
        self.assertEqual(opposite_direction(Direction.LEFT), Direction.RIGHT)
        self.assertEqual(opposite_direction(Direction.RIGHT), Direction.LEFT)

    def test_distance(self):
        self.assertEqual(distance((0,0),(3,4)), 5)
        self.assertEqual(distance((3,4), (0,0)), 5)
        self.assertEqual(distance((-3,0), (0,4)), 5)
        self.assertEqual(distance((0,0), (0,4)), 4)


if __name__ == '__main__':
    unittest.main()