import sys

sys.path.append("../../AoC2022")

from input_parser import get_input
from collections import namedtuple
import math

Position = namedtuple("Position", "x y")

class Knot:

    def __init__(self):
        self.x = 0
        self.y = 0
        
    def move_position(self, pos):
        self.x += pos.x
        self.y += pos.y
        
        return self.get_position()

    def get_position(self):
        return Position(self.x, self.y)
        
    def chase_knot(self, pos):
        if self.is_adjacent(pos):
            return self.get_position()
            
        chase = lambda t, h: h if (t+h)%2 else (t+h)//2
        
        self.x = chase(self.x, pos.x)
        self.y = chase(self.y, pos.y)
        
        return self.get_position()
        
    def is_adjacent(self, pos):
        x_dist = abs(self.x - pos.x)
        y_dist = abs(self.y - pos.y)

        return True if x_dist <= 1 and y_dist <= 1 else False
        
    
def main(input_lines, rope_size=10):
    # head at idx 0, tail at idx -1
    rope = [Knot() for _ in range(rope_size)]
    head = rope[0]
    tail = rope[-1]
    
    tail_hist = set()
    
    for line in input_lines:
        direction, num_move_spots = line.split(' ')
        num_move_spots = int(num_move_spots)
        
        move_table = {'R':(1,0), 'D':(0,-1), 'L':(-1,0), 'U':(0,1)}
        move_pos = Position(*move_table[direction])
        
        for _ in range(num_move_spots):
            leader = head.move_position(move_pos)

            for knot_num in range(1, len(rope)):
                follower = rope[knot_num].chase_knot(leader)
                leader = follower
                
            tail_hist.add(tail.get_position())
            
    print(len(tail_hist))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        rope_size = int(sys.argv[1])
    else:
        rope_size = 2
    input_lines = get_input()
    main(input_lines, rope_size)