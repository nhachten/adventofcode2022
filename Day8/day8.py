
import sys

sys.path.append("../../AoC2022")

from collections import namedtuple

from input_parser import get_input
from pprint import pprint

Position = namedtuple("Position", "x y")
TallNeighbor = namedtuple("TallNeighbor", "height pos")

peek_table = {}

def get_index(pos, direction):
    if direction == "right" or direction == "left":
        return pos.y
    else:
        return pos.x

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
        
def peek(pos, direction, from_height=10):
    #if pos not in peek_table:
    #	peek_table[pos] = {}
        
    cur_height = int(input_lines[pos.x][pos.y])
    
    #if direction in peek_table[pos]:
    #	#return max(cur_height, peek_table[pos][direction])
    #    if cur_height > peek_table[pos][direction].height:
    #        #return TallNeighbor(cur_height, get_index(pos, direction))
    #        return TallNeighbor(cur_height, pos)
    #    else:
    #	    return peek_table[pos][direction]
        
    new_pos = update_position(pos, direction)
    if new_pos == None or cur_height >= from_height:
        #return cur_height
        #return TallNeighbor(cur_height, get_index(pos, direction))
        return TallNeighbor(cur_height, pos)
        
    tallest_neighbor = peek(new_pos, direction)
    #peek_table[pos][direction] = tallest_neighbor
    
    #return max(tallest_neighbor, cur_height)
    if cur_height >= tallest_neighbor.height:
        #return TallNeighbor(cur_height, get_index(pos, direction))
        return TallNeighbor(cur_height, pos)
    else:
        return tallest_neighbor

def height(pos):
    return int(input_lines[pos.x][pos.y])

def peek2(pos, direction):
    start_height = height(pos)
    los_dist = 0

    next_pos = update_position(pos, direction)

    while next_pos:
        los_dist += 1
        if start_height <= height(next_pos):
            break
        next_pos = update_position(next_pos, direction)

    return los_dist, next_pos

def part2(input_lines):
    directions = ["right", "down", "left", "up"]
    vis_list = []
    for x in range(0, len(input_lines)):
        for y in range(0, len(input_lines[0])):
            pos = Position(x,y)
            vis_score = 1
            for d in directions:
                los_dist, tree_blocking_view = peek2(pos, d)
                vis_score *= los_dist
            vis_list.append(vis_score)

    vis_list.sort()
    print(vis_list[-1])

    
def main(input_lines):
    part2(input_lines)
    return 0
    number_visible = len(input_lines) * len(input_lines[0])
    directions = ["right", "down", "left", "up"]
    vis_score_list = []
    
    for x in range(1, len(input_lines) - 1):
        for y in range(1, len(input_lines[0]) - 1):
            cur_height = int(input_lines[x][y])
            pos = Position(x,y)
            hidden = True # for part 1
            vis_score = 1 # for part 2
            print("########")
            for d in directions:
                tallest_neighbor = peek(update_position(pos, d), d, cur_height)
                #tallest_neighbor = peek_table[pos][d]
                print(f"pos: {pos}")
                print(f"dir: {d}")
                print(f"tn: {tallest_neighbor}")
                print()
                if tallest_neighbor.height < cur_height:
                    if d == "right":
                        vis_score *= len(input_lines) - pos.x - 1
                    elif d == "left":
                        vis_score *= pos.x
                    elif d == "down":
                        vis_score *= len(input_lines[0]) - pos.y - 1
                    elif d == "up":
                        vis_score *= pos.y
                    hidden = False
                    #break
                else:
                    if d == "right":
                        vis_score *= tallest_neighbor.pos.x - pos.x
                    elif d == "left":
                        vis_score *= pos.x - tallest_neighbor.pos.x
                    elif d == "down":
                        vis_score *= tallest_neighbor.pos.y -  pos.y
                    elif d == "up":
                        vis_score *= pos.y - tallest_neighbor.pos.y
                print(f"vs: {vis_score}")
            vis_score_list.append(vis_score)
            print(f"pos: {pos}")
            print(f"vs: {vis_score}")
                
            if hidden:
                number_visible -= 1
            

    # part 1            
    print(number_visible)
    # part 2
    vis_score_list.sort()
    print(vis_score_list[-1])

if __name__ == "__main__":
    #input_lines = get_input("tiny_input.txt")
    input_lines = get_input()
    main(input_lines)