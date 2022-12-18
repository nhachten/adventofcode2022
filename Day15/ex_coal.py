
from pprint import pprint
import sys

sys.path.append("../../AoC2022")

from input_parser import get_input
import re

pat = "-?\d+"

list_of_empty_col_ranges_by_row_lookup_dict = {}

def coalesce(list_of_ranges):
    index = 0
    while index < len(list_of_ranges) - 1:
        print(f"index: {index}")
        left = list_of_ranges[index]
        right = list_of_ranges[index + 1]
        print(f"left: {left}")
        print(f"right: {right}")
        if left.stop >= right.start:
            new_range = range(left.start, max(left.stop, right.stop))
            print(f"new_range: {new_range}")
            list_of_ranges[index] = new_range
            list_of_ranges = list_of_ranges[:index+1] + list_of_ranges[index+2:]
            print(f"list_of_ranges: {list_of_ranges}")
        else:
            index += 1

    return list_of_ranges

def add_range_to_list(list_of_ranges, r):
    i = 0
    while True:
        try:
            if list_of_ranges[i].start > r.start:
                break
        except:
            break
        i += 1

    list_of_ranges.insert(i, r)
    list_of_ranges = coalesce(list_of_ranges)
    return list_of_ranges

def process_sensor_beacon_pair(sbp_pair):
    sx, sy, bx, by = sbp_pair
    md = abs(sx - bx) + abs(sy - by)

    for dist_from_sensor_row in range(-md, md + 1):
        x = sx + dist_from_sensor_row

        empty_cols = range(sy - (md - abs(dist_from_sensor_row)), sy + ( md - abs(dist_from_sensor_row)) + 1)
        #row_info[x].add_empty_spaces(empty_cols)
        if x not in list_of_empty_col_ranges_by_row_lookup_dict:
            list_of_empty_col_ranges_by_row_lookup_dict[x] = []
        list_of_empty_col_ranges_by_row_lookup_dict[x] = add_range_to_list(list_of_empty_col_ranges_by_row_lookup_dict[x], empty_cols)

def main(input_lines):
    for line in input_lines:
        sensor_beacon_pair = list(map(int, re.findall(pat, line)))
        process_sensor_beacon_pair(sensor_beacon_pair)

    pprint(list_of_empty_col_ranges_by_row_lookup_dict)

if __name__ == "__main__":
    input_lines = get_input("tiny_input.txt")
    main(input_lines)