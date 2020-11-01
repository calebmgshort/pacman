from constants import *
from typing import List, Tuple

class ValidCharacterLocations():
    __valid_horizontal_locs = dict()
    __valid_horizontal_locs[LANE_HORIZONTAL_1_LATTITUDE] = [(LANE_VERTICAL_1_LONGITUDE, LANE_VERTICAL_5_LONGITUDE), (LANE_VERTICAL_6_LONGITUDE, LANE_VERTICAL_10_LONGITUDE)]
    __valid_horizontal_locs[LANE_HORIZONTAL_2_LATTITUDE] = [(LANE_VERTICAL_1_LONGITUDE, LANE_VERTICAL_10_LONGITUDE)]
    __valid_horizontal_locs[LANE_HORIZONTAL_3_LATTITUDE] = [(LANE_VERTICAL_1_LONGITUDE, LANE_VERTICAL_3_LONGITUDE), (LANE_VERTICAL_4_LONGITUDE, LANE_VERTICAL_5_LONGITUDE), (LANE_VERTICAL_6_LONGITUDE, LANE_VERTICAL_7_LONGITUDE), (LANE_VERTICAL_8_LONGITUDE, LANE_VERTICAL_10_LONGITUDE)]
    __valid_horizontal_locs[LANE_HORIZONTAL_4_LATTITUDE] = [(LANE_VERTICAL_4_LONGITUDE, LANE_VERTICAL_7_LONGITUDE)]
    __valid_horizontal_locs[LANE_HORIZONTAL_5_LATTITUDE] = [(LANE_VERTICAL_1_LONGITUDE-THIN_WALL_THICKNESS, LANE_VERTICAL_4_LONGITUDE), (LANE_VERTICAL_5_LONGITUDE-THIN_WALL_THICKNESS, LANE_VERTICAL_6_LONGITUDE+THIN_WALL_THICKNESS), (LANE_VERTICAL_7_LONGITUDE, LANE_VERTICAL_10_LONGITUDE + THIN_WALL_THICKNESS)]
    __valid_horizontal_locs[LANE_HORIZONTAL_6_LATTITUDE] = __valid_horizontal_locs[LANE_HORIZONTAL_4_LATTITUDE]
    __valid_horizontal_locs[LANE_HORIZONTAL_7_LATTITUDE] = __valid_horizontal_locs[LANE_HORIZONTAL_1_LATTITUDE]
    __valid_horizontal_locs[LANE_HORIZONTAL_8_LATTITUDE] = [(LANE_VERTICAL_1_LONGITUDE, LANE_VERTICAL_2_LONGITUDE), (LANE_VERTICAL_3_LONGITUDE, LANE_VERTICAL_8_LONGITUDE), (LANE_VERTICAL_9_LONGITUDE, LANE_VERTICAL_10_LONGITUDE)]
    __valid_horizontal_locs[LANE_HORIZONTAL_9_LATTITUDE] = __valid_horizontal_locs[LANE_HORIZONTAL_3_LATTITUDE]
    __valid_horizontal_locs[LANE_HORIZONTAL_10_LATTITUDE] = __valid_horizontal_locs[LANE_HORIZONTAL_2_LATTITUDE]

    __valid_vertical_locs = dict()
    __valid_vertical_locs[LANE_VERTICAL_1_LONGITUDE] = [(LANE_HORIZONTAL_1_LATTITUDE, LANE_HORIZONTAL_3_LATTITUDE), (LANE_HORIZONTAL_7_LATTITUDE, LANE_HORIZONTAL_8_LATTITUDE), (LANE_HORIZONTAL_9_LATTITUDE, LANE_HORIZONTAL_10_LATTITUDE)]
    __valid_vertical_locs[LANE_VERTICAL_2_LONGITUDE] = [(LANE_HORIZONTAL_8_LATTITUDE, LANE_HORIZONTAL_9_LATTITUDE)]
    __valid_vertical_locs[LANE_VERTICAL_3_LONGITUDE] = [(LANE_HORIZONTAL_1_LATTITUDE, LANE_HORIZONTAL_9_LATTITUDE)]
    __valid_vertical_locs[LANE_VERTICAL_4_LONGITUDE] = [(LANE_HORIZONTAL_2_LATTITUDE, LANE_HORIZONTAL_3_LATTITUDE), (LANE_HORIZONTAL_4_LATTITUDE, LANE_HORIZONTAL_7_LATTITUDE), (LANE_HORIZONTAL_8_LATTITUDE, LANE_HORIZONTAL_9_LATTITUDE)]
    __valid_vertical_locs[LANE_VERTICAL_5_LONGITUDE] = [(LANE_HORIZONTAL_1_LATTITUDE, LANE_HORIZONTAL_2_LATTITUDE), (LANE_HORIZONTAL_3_LATTITUDE, LANE_HORIZONTAL_4_LATTITUDE), (LANE_HORIZONTAL_7_LATTITUDE, LANE_HORIZONTAL_8_LATTITUDE), (LANE_HORIZONTAL_9_LATTITUDE, LANE_HORIZONTAL_10_LATTITUDE)]
    __valid_vertical_locs[LANE_VERTICAL_5_5_LONGITUDE] = [(LANE_HORIZONTAL_4_LATTITUDE, LANE_HORIZONTAL_5_LATTITUDE)]
    __valid_vertical_locs[LANE_VERTICAL_6_LONGITUDE] = __valid_vertical_locs[LANE_VERTICAL_5_LONGITUDE]
    __valid_vertical_locs[LANE_VERTICAL_7_LONGITUDE] = __valid_vertical_locs[LANE_VERTICAL_4_LONGITUDE]
    __valid_vertical_locs[LANE_VERTICAL_8_LONGITUDE] = __valid_vertical_locs[LANE_VERTICAL_3_LONGITUDE]
    __valid_vertical_locs[LANE_VERTICAL_9_LONGITUDE] = __valid_vertical_locs[LANE_VERTICAL_2_LONGITUDE]
    __valid_vertical_locs[LANE_VERTICAL_10_LONGITUDE] = __valid_vertical_locs[LANE_VERTICAL_1_LONGITUDE]

    @staticmethod
    def __val_in_list(value: float, ranges: List[Tuple[float, float]]) -> bool:
        for endpoints in ranges: 
            if value >= endpoints[0] and value <= endpoints[1]:
                return True
        return False

    @staticmethod
    def valid_coordinates(coordinates: Tuple[float, float]) -> bool:
        if coordinates[1] in ValidCharacterLocations.__valid_horizontal_locs:
            if ValidCharacterLocations.__val_in_list(coordinates[0], ValidCharacterLocations.__valid_horizontal_locs[coordinates[1]]):
                return True
        if coordinates[0] in ValidCharacterLocations.__valid_vertical_locs:
            if ValidCharacterLocations.__val_in_list(coordinates[1], ValidCharacterLocations.__valid_vertical_locs[coordinates[0]]):
                return True
        return False
