import unittest
from valid_character_locations import ValidCharacterLocations
from constants import *

class TestValidCharacterLocations(unittest.TestCase):
    def test_valid_coordinates(self):
        # On horizontal paths
        self.assertTrue(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_1_LATTITUDE)))
        self.assertTrue(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_1_LONGITUDE + LANE_SIZE/2 + 0.1, LANE_HORIZONTAL_1_LATTITUDE)))
        self.assertTrue(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_6_LONGITUDE + LANE_SIZE, LANE_HORIZONTAL_4_LATTITUDE)))
        self.assertTrue(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_1_LONGITUDE - THIN_WALL_THICKNESS, LANE_HORIZONTAL_5_LATTITUDE)))
        self.assertTrue(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_5_LONGITUDE - THIN_WALL_THICKNESS, LANE_HORIZONTAL_5_LATTITUDE)))

        # On vertical paths
        self.assertTrue(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_1_LATTITUDE + LANE_SIZE/2)))
        self.assertTrue(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_10_LONGITUDE, LANE_HORIZONTAL_10_LATTITUDE - LANE_SIZE/2)))
        self.assertTrue(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_4_LONGITUDE, LANE_HORIZONTAL_6_LATTITUDE + CHARACTER_SPEED)))

        # Invalid locations
        self.assertFalse(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_1_LONGITUDE - 1, LANE_HORIZONTAL_1_LATTITUDE)))
        self.assertFalse(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_1_LATTITUDE - 1)))
        self.assertFalse(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_10_LONGITUDE, LANE_HORIZONTAL_10_LATTITUDE + 0.2)))
        self.assertFalse(ValidCharacterLocations.valid_coordinates((LANE_VERTICAL_5_LONGITUDE - THIN_WALL_THICKNESS - 0.1, LANE_HORIZONTAL_5_LATTITUDE)))

    def test_on_intersection(self):
        # 0 valid outgoing locations: not intersection
        self.assertFalse(ValidCharacterLocations.on_intersection((LANE_VERTICAL_1_LONGITUDE + LANE_SIZE, LANE_HORIZONTAL_1_LATTITUDE + LANE_SIZE)))
        # 1 valid outgoing locations: not intersection
        self.assertFalse(ValidCharacterLocations.on_intersection((LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_1_LATTITUDE + LANE_SIZE)))
        # 2 valid outgoing locations: not intersection
        self.assertFalse(ValidCharacterLocations.on_intersection((LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_1_LATTITUDE)))
        # 3 valid outgoing locations: yes, intersection
        self.assertTrue(ValidCharacterLocations.on_intersection((LANE_VERTICAL_5_LONGITUDE, LANE_HORIZONTAL_2_LATTITUDE)))
        # 4 valid outgoing locations: yes, intersection
        self.assertTrue(ValidCharacterLocations.on_intersection((LANE_VERTICAL_3_LONGITUDE, LANE_HORIZONTAL_2_LATTITUDE)))

        # Extra tests
        self.assertTrue(ValidCharacterLocations.on_intersection((LANE_VERTICAL_1_LONGITUDE, LANE_HORIZONTAL_2_LATTITUDE)))

    def test_random_valid_coordinates(self):
        for i in range(0, 10):
            self.assertTrue(ValidCharacterLocations.valid_coordinates(ValidCharacterLocations.random_valid_coordinates()))


if __name__ == '__main__':
    unittest.main()