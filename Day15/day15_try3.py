import sys

sys.path.append("../../AoC2022")

from input_parser import get_input
import re

pat = "-?\d+"

from collections import namedtuple


#sbp_list = []
row_info = {}

class RowInfo:

    def __init__(self):
        self.empty = set()
        self.beacons = set()
        self.sensors = set()

    def add_empty_spaces(self, empty_set):
        # TODO coalesce
        self.empty.add(empty_set)

    def __str__(self):
        return f"empty: {self.empty}"
    

def process_sensor_beacon_pair(sbp_pair):
    sx, sy, bx, by = sbp_pair
    md = abs(sx - bx) + abs(sy - by)

    for dist_from_sensor_row in range(-md, md + 1):
        x = sx + dist_from_sensor_row
        if x not in row_info:
            row_info[x] = RowInfo()

        #empty_cols = (sy -(md - abs(dist_from_sensor_row)), sy + (md - abs(dist_from_sensor_row)) + 1)
        empty_cols = (sy - (md - abs(dist_from_sensor_row)), sy + ( md - abs(dist_from_sensor_row)) + 1)
        row_info[x].add_empty_spaces(empty_cols)



def count_row_intersect(row_num):
    total_overlap = set()
    for sx, sy, bx, by in sbp_list:
        md = abs(sx - bx) + abs(sy - by)
        #print(f"sensor ({sx},{sy}) - beacon ({bx},{by}) - md: {md}")
        if (sy-md) <= row_num <= (sy+md):
            #print("add to overlap")
            overlap = range(sx - (md - abs(row_num-sy)), sx + (md - abs(row_num-sy)) + 1)
            overlap_list = [(x, row_num) for x in overlap]
            #print(overlap)
            #total_overlap.update(overlap)
            total_overlap.update(overlap_list)
            total_overlap.discard((bx, by))
            #if row_num == bx:
            #    total_overlap.discard(by)

    #print(total_overlap)
    print(len(total_overlap))
    return total_overlap



def main(input_lines):
    for line in input_lines:
        sensor_beacon_pair = list(map(int, re.findall(pat, line)))
        process_sensor_beacon_pair(sensor_beacon_pair)

    #print(row_info)
    for row_key, row_val in row_info.items():
        print(f"{row_key}: {row_val}")

    for x in range(0, 21):
        print(f"{x:<3}", end="")
       # for y in range(y_min, y_max + 1):
        for y in range(0, 21):
            #if (x,y) in known_beacons:
            if y in row_info[x].beacons:
                print("B",end="")
            #elif (x,y) in known_sensors:
            elif y in row_info[x].sensors:
                print("S",end="")
            #elif (x,y) in known_empty_space:
            elif y in row_info[x].empty:
                print("#",end="")
            else:
                print(".",end="")
                    
        print()


if __name__ == "__main__":
    input_lines = get_input("tiny_input.txt")
    #input_lines = get_input()
    main(input_lines)