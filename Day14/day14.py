import sys

sys.path.append("../../AoC2022")

from input_parser import get_input

from collections import namedtuple
from pprint import pprint

Position = namedtuple("Position", "right down")
SAND_DROP = Position(500, 0)

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

def blocked(position):
    if position in rock_positions or position in sand_positions:
        return True 
    else:
        return False

def drop_sand():
    current_position = SAND_DROP
    still_falling = True
    inf_fall_check = 0 # TODO check for fall beyond greatest down rock

    while still_falling:
        if not blocked(Position(current_position.right, current_position.down + 1)):
            current_position = Position(current_position.right, current_position.down + 1)
        elif not blocked(Position(current_position.right - 1, current_position.down + 1)):
            current_position = Position(current_position.right - 1, current_position.down + 1)
        elif not blocked(Position(current_position.right + 1, current_position.down + 1)):
            current_position = Position(current_position.right + 1, current_position.down + 1)
        else:
            still_falling = False
            # TODO make a temp set to add at the end, if bottom out then don't add it, maybe add to a 
            # new set for infinite path
            sand_positions.add(current_position)
        inf_fall_check += 1

        # TODO check against the bottom
        if inf_fall_check > 1000:
            print("Detected infinite fall")
            return False

    return True

def main(input_lines):
    # TODO find the bottom
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


if __name__ == "__main__":
    input_lines = get_input("tiny_input.txt")
    main(input_lines)