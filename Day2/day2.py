import sys

sys.path.append("../../AoC2022")

from input_parser import get_input

def part1(input_lines):
    lookup_table = {
        "A X": 4, # rock and rock is 1 plus 3 for draw
        "A Y": 8, # rock and paper is 2 plus 6 for win
        "A Z": 3, # rock and scissor is 3 plus 0 for loss
        "B X": 1, # paper and rock is 1 plus 0 for loss
        "B Y": 5, # paper and paper is 2 plus 3 for draw
        "B Z": 9, # paper and scissor is 3 plus 6 for win
        "C X": 7, # scissor and rock is 1 plus 6 for win
        "C Y": 2, # scissor and paper is 2 plus 0 for loss
        "C Z": 6  # scissor and scissor is 3 plus 3 for draw
    }

    total_score = 0

    for line in input_lines:
        total_score += lookup_table[line]

    print(total_score)

def part2(input_lines):
    lookup_table = {
        "A X": 3, # opp picks R, need lose, I pick S, 0 + 3
        "A Y": 4, # opp picks R, need draw, I pick R, 3 + 1
        "A Z": 8, # opp picks R, need win, I pick P, 6 + 2
        "B X": 1, # opp picks P, need lose, I pick R, 0 + 1
        "B Y": 5, # opp picks P, need draw, I pick P, 3 + 2
        "B Z": 9, # opp picks P, need win, I pick S, 6 + 3
        "C X": 2, # opp picks S, need lose, I pick P, 0 + 2
        "C Y": 6, # opp picks S, need draw, I pick S, 3 + 3
        "C Z": 7  # opp picks S, need win, I pick R, 6 + 1
    }

    total_score = 0

    for line in input_lines:
        total_score += lookup_table[line]

    print(total_score)

def main(input_lines):
    part2(input_lines)
    

if __name__ == "__main__":
    input_lines = get_input()
    main(input_lines)