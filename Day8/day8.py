
import sys

sys.path.append("../../AoC2022")

from collections import namedtuple

from input_parser import get_input
from pprint import pprint

Position = namedtuple("Position", "x y")

def update_position(pos, direction):
    if direction == "right":
        new_pos = Position(pos.x + 1, pos.y)
    elif direction == "down":
        new_pos = Position(pos.x, pos.y + 1)
    elif direction == "left":
        new_pos = Position(pos.x - 1, pos.y)
    else: # "up"
        new_pos = Position(pos.x, pos.y - 1)
        
    if new_pos.x < 0 or new_pos.x >= len(input_lines) or \
        new_pos.y < 0 or new_pos.y >= len(input_lines[0]):
        return None
    else:
        return new_pos
        
def height(pos):
    return int(input_lines[pos.x][pos.y])

def peek(pos, direction):
    start_height = height(pos)
    los_dist = 0

    next_pos = update_position(pos, direction)

    while next_pos:
        los_dist += 1
        if start_height <= height(next_pos):
            break
        next_pos = update_position(next_pos, direction)

    return los_dist, next_pos

def main(input_lines):
    directions = ["right", "down", "left", "up"]
    vis_list = []
    hidden_set = set()
    for x in range(0, len(input_lines)):
        for y in range(0, len(input_lines[0])):
            pos = Position(x,y)
            vis_score = 1
            hidden = True
            for d in directions:
                los_dist, tree_blocking_view = peek(pos, d)
                vis_score *= los_dist
                if not tree_blocking_view:
                    hidden = False
            if hidden:
                hidden_set.add(pos)
            vis_list.append(vis_score)

    print("part 1")
    number_visible = len(input_lines) * len(input_lines[0]) - len(hidden_set)
    print(number_visible)
    print("part 2")
    vis_list.sort()
    print(vis_list[-1])


if __name__ == "__main__":
    input_lines = get_input()
    main(input_lines)