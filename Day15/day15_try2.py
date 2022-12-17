import sys

sys.path.append("../../AoC2022")

from input_parser import get_input
import re

pat = "-?\d+"

sbp_list = []

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

def count_col_intersect(row_num):
    total_overlap = set()
    for sx, sy, bx, by in sbp_list:
        md = abs(sx - bx) + abs(sy - by)
        #print(f"sensor ({sx},{sy}) - beacon ({bx},{by}) - md: {md}")
        if (sx-md) <= row_num <= (sx+md):
            #print("add to overlap")
            #overlap = range(sy - (md - abs(row_num-sx)), sy + (md - abs(row_num-sx)) + 1)
            #overlap_list = [(row_num, y) for y in overlap]
            #print(overlap)
            #total_overlap.update(overlap)
            total_overlap.update(overlap_list)
            total_overlap.discard((bx, by))
            #if row_num == bx:
            #    total_overlap.discard(by)

    #print(total_overlap)
    print(len(total_overlap))

#    sensor_x, sensor_y, beacon_x, beacon_y = sensor_beacon_pair
#    md = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
#    
#    for x in range(-md, md + 1):
#        for y in range(-(md - abs(x)), (md - abs(x)) + 1):
#            known_empty_space.add((sensor_x + x, sensor_y + y))
#
#    known_empty_space.remove((beacon_x, beacon_y))


def main(input_lines):
    for line in input_lines:
        sensor_beacon_pair = list(map(int, re.findall(pat, line)))
        sbp_list.append(sensor_beacon_pair)

    s1 = set(list(zip(*count_row_intersect(2000000)))[0])
    #s2 = set(list(zip(*count_row_intersect(2000001)))[0])

   # print(s1.difference(s2))
        
    

if __name__ == "__main__":
    #input_lines = get_input("tiny_input.txt")
    input_lines = get_input()
    main(input_lines)