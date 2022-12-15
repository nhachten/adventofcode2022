import sys

sys.path.append("../../AoC2022")

from input_parser import get_input

from collections import namedtuple
from pprint import pprint

Position = namedtuple("Position", "right down")
SAND_DROP = Position(500, 0)

right_low_bound = 999999
right_high_bound = 0
down_high_bound = 0 

rock_positions = set()
sand_positions = set()

def place_rocks(start, end):
    if start.right == end.right:
        if start.down <= end.down:
            inc_step = 1
        else:
            inc_step = -1
        rock_positions.update({Position(start.right,d) for d in range(start.down, end.down + inc_step, inc_step)}) 
    elif start.down == end.down:
        if start.right <= end.right:
            inc_step = 1
        else:
            inc_step = -1
        rock_positions.update({Position(r,start.down) for r in range(start.right, end.right + inc_step, inc_step)}) 

    global right_low_bound
    global right_high_bound
    global down_high_bound

    if start.right < right_low_bound:
        right_low_bound = start.right
    if end.right < right_low_bound:
        right_low_bound = end.right

    if start.right > right_high_bound:
        right_high_bound = start.right
    if end.right > right_high_bound:
        right_high_bound = end.right

    if start.down > down_high_bound:
        down_high_bound = start.down
    if end.down > down_high_bound:
        down_high_bound = end.down

def blocked(position):
    if position in rock_positions or position in sand_positions:
        return True 
    else:
        return False

def drop_sand():
    current_position = SAND_DROP
    still_falling = True

    while still_falling:
        if not blocked(Position(current_position.right, current_position.down + 1)):
            current_position = Position(current_position.right, current_position.down + 1)
        elif not blocked(Position(current_position.right - 1, current_position.down + 1)):
            current_position = Position(current_position.right - 1, current_position.down + 1)
        elif not blocked(Position(current_position.right + 1, current_position.down + 1)):
            current_position = Position(current_position.right + 1, current_position.down + 1)
        else:
            still_falling = False
            sand_positions.add(current_position)

        if current_position.down > down_high_bound:
            print("Detected infinite fall")
            return False

    return True

def main(input_lines):
    for line in input_lines:
        rock_lines = line.split(" -> ")
        start = Position(*list(map(int,rock_lines[0].split(','))))
        for rock_line in rock_lines[1:]:
            end = Position(*list(map(int,rock_line.split(','))))
            place_rocks(start, end)
            start = end

    sand_stopped = True
    while sand_stopped:
        sand_stopped = drop_sand()

    pprint(sand_positions)
    print(len(sand_positions))

    for down in range(0, down_high_bound + 1):
        for right in range(right_low_bound, right_high_bound + 1):
            if Position(right,down) in sand_positions:
                print("o",end="")
            elif Position(right,down) in rock_positions:
                print("#",end="")
            else:
                print(".",end="")

        print()



if __name__ == "__main__":
    #input_lines = get_input("tiny_input.txt")
    input_lines = get_input()
    main(input_lines)