import sys

sys.path.append("../../AoC2022")

from input_parser import get_input
from queue import Queue
from collections import namedtuple

Position = namedtuple("Position", "row col")
Stamp = namedtuple("Stamp", "position via distance")

q = Queue()
visited = set()
stamp_table = {}

def can_climb(from_pos, to_pos, input_lines):
    in_bounds = lambda pos: True if 0<= pos.row < len(input_lines) and 0 <= pos.col < len(input_lines[0]) else False
    
    if not in_bounds(to_pos):
        return False
    
    #convert_height = lambda spec_char, height_char, input_char: height_char if input_char == spec_char else input_char
    
    from_height = input_lines[from_pos.row][from_pos.col]
    to_height = input_lines[to_pos.row][to_pos.col]
    
    from_height = 'a' if from_height == 'S' else from_height
    to_height = 'z' if to_height == 'E' else to_height
    
    return True if ord(to_height) - ord(from_height) <= 1 else False
    
def visit(stamp, input_lines):
    visited.add(stamp.position)
    stamp_table[stamp.position] = stamp # or maybe this should be a set
    
    move_table = {"up": (0,-1), "right": (1,0), "down": (0,1), "left": (-1,0)}
    
    for move in move_table.values():
        move_pos = Position(*move)
        new_pos = Position(stamp.position.row + move_pos.row, stamp.position.col + move_pos.col)
        if can_climb(stamp.position, new_pos, input_lines):
            q.put(Stamp(new_pos, stamp.position, stamp.distance + 1))

def is_end(stamp, input_lines):
    if input_lines[stamp.position.row][stamp.position.col] == 'E':
        d = stamp.distance
        print(f"Found end in {stamp.distance} steps")
        return True, d

    return False, -1
            
def main(input_lines):

    # find all a squares
    a_squares = []
    for r in range(40):
        for c in range(100):
            if input_lines[r][c] == 'a':
                a_squares.append(Position(r,c))

    best_distance = 100000
    for a_square in a_squares:
        visited.clear()
        q.queue.clear()
        start_pos = a_square
        first_stamp = Stamp(start_pos, None, 0)
        q.put(first_stamp)
        
        found = False
        while not q.empty() and not found:
            stamp = q.get()
            if stamp.position not in visited:
                #print(f"visit {stamp} with elevation {input_lines[stamp.position.row][stamp.position.col]}")
                visit(stamp, input_lines)
                found_end, distance = is_end(stamp, input_lines)
                #if is_end(stamp, input_lines):
                if found_end:
                    print(f"found end with distance {distance}")
                    if distance < best_distance:
                        best_distance = distance
                    found = True

    print(best_distance)

    # display the visited squares
    #for r in range(0,40):
    #    for c in range(0,100):
    #        if Position(r,c) in visited:
    #            print(input_lines[r][c],end='')
    #        else:
    #            print('.',end='')
    #    print()
    
if __name__ == "__main__":
    #input_lines = get_input("tiny_input.txt")
    input_lines = get_input()
    main(input_lines)