import sys

sys.path.append("../../AoC2022")

from input_parser import get_input
import re

pat = "-?\d+"

known_empty_space = set()
known_beacons = set()
known_sensors = set()

def mark_empty_space(sensor_beacon_pair):
    sensor_x, sensor_y, beacon_x, beacon_y = sensor_beacon_pair
    md = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    
    for x in range(-md, md + 1):
        for y in range(-(md - abs(x)), (md - abs(x)) + 1):
            known_empty_space.add((sensor_x + x, sensor_y + y))

    known_empty_space.remove((beacon_x, beacon_y))

    
def main(input_lines):
    for line in input_lines:
        sensor_beacon_pair = list(map(int, re.findall(pat, line)))
        mark_empty_space(sensor_beacon_pair)
        known_beacons.add((sensor_beacon_pair[2], sensor_beacon_pair[3]))
        known_sensors.add((sensor_beacon_pair[0], sensor_beacon_pair[1]))
        
    x_max, y_max = map(max, zip(*known_empty_space))
    x_min, y_min = map(min, zip(*known_empty_space))

    #for y in range(y_min, y_max + 1, 5):
    for y in range(0, 21, 5):
        print("{:>5}".format(y), end="")
    print()
    #for x in range(x_min, x_max + 1):
    for x in range(0, 21):
        print(f"{x:<3}", end="")
       # for y in range(y_min, y_max + 1):
        for y in range(0, 21):
            if (x,y) in known_beacons:
                print("B",end="")
            elif (x,y) in known_sensors:
                print("S",end="")
            elif (x,y) in known_empty_space:
                print("#",end="")
            else:
                print(".",end="")
                    
        print()
            
    row_number = 10
    count_in_row_n = sum([n == row_number for n in list(zip(*known_empty_space))[0]])
    print(count_in_row_n)

if __name__ == "__main__":
    input_lines = get_input("tiny_input.txt")
    #input_lines = get_input()
    main(input_lines)