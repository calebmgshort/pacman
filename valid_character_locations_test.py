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

if __name__ == '__main__':
    unittest.main()