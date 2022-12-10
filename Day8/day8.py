
import sys

sys.path.append("../../AoC2022")

from collections import namedtuple

from input_parser import get_input
from pprint import pprint

Position = namedtuple("Position", "x y")

peek_table = {}

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
        
def peek(pos, direction):
    if pos not in peek_table:
    	peek_table[pos] = {}
        
    cur_height = int(input_lines[pos.x][pos.y])
    
    if direction in peek_table[pos]:
    	return max(cur_height, peek_table[pos][direction])
        
    new_pos = update_position(pos, direction)
    if new_pos == None:
        return cur_height
        
    tallest_neighbor = peek(new_pos, direction)
    peek_table[pos][direction] = tallest_neighbor
    
    return max(tallest_neighbor, cur_height)
    
def main(input_lines):
    number_visible = len(input_lines) * len(input_lines[0])
    print(len(input_lines))
    print(len(input_lines[0]))
    print(number_visible)
    directions = ["right", "down", "left", "up"]
    
    for x in range(1, len(input_lines) - 1):
        for y in range(1, len(input_lines[0]) - 1):
            cur_height = int(input_lines[x][y])
            pos = Position(x,y)
            hidden = True
            for d in directions:
                peek(pos, d)
                tallest_neighbor = peek_table[pos][d]
                if tallest_neighbor < cur_height:
                    hidden = False
                    break
            if hidden:
                number_visible -= 1
                
    print(number_visible)

if __name__ == "__main__":
    input_lines = get_input()
    main(input_lines)