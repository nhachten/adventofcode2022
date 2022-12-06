import sys

sys.path.append("../../AoC2022")

from input_parser import get_input

from collections import namedtuple
from pprint import pprint

Move = namedtuple("Move", "num_to_move src dst")

def process_move(stacks, move, part=1):
    t = stacks[move.src][-move.num_to_move:]
    stacks[move.src] = stacks[move.src][:-move.num_to_move]
    if part == 1:
        t.reverse()
    elif part != 2:
        raise Exception("Must be part 1 or part 2")
    stacks[move.dst] += t

def main(input_lines, part):
    i = 0
    stacks = []
    moves = []
    for line in input_lines:
        cur_col = 0
        text_col_pos = 1

        # process stacks
        if '[' in line:
            while text_col_pos < len(line):
                try:
                    if line[text_col_pos] != ' ':
                        stacks[cur_col].append(line[text_col_pos])
                    text_col_pos += 4
                    cur_col += 1
                except IndexError:
                    stacks.append([])

        elif 'move' in line:
            line_spl = line.split('move')[1].split('from') # [' 8 ', ' 5 to 8']
            num_to_move = int(line_spl[0].strip())
            line_spl = line_spl[1].split('to')
            source_col = int(line_spl[0].strip()) - 1
            dest_col = int(line_spl[1].strip()) - 1
            
            moves.append(Move(num_to_move, source_col, dest_col))

    # reverse the stacks so that we can use pop() to remove the items from the top i.e. put the top item 
    # at the end of th list
    for stack in stacks:
        stack.reverse()

    for move in moves:
        process_move(stacks, move, part)

    for stack in stacks:
        print(stack[-1], end='')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        part = int(sys.argv[1])
    else:
        part = 1
    input_lines = get_input()
    main(input_lines, part)