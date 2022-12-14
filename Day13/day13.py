import sys

sys.path.append("../../AoC2022")

from input_parser import get_input

import json

def is_correct_order(left, right):
    #print(f"correct order {left} {right}")
    correct_order = True
    try:
        for i in range(len(left)):
            #print(f"compare {left[i]} to {right[i]}")
            if isinstance(left[i],list) or isinstance(right[i],list):
                if not isinstance(left[i],list):
                    correct_order = is_correct_order([left[i]], right[i])
                elif not isinstance(right[i],list):
                    correct_order = is_correct_order(left[i], [right[i]])
                else:
                    correct_order = is_correct_order(left[i], right[i])
            else:
                if left[i] > right[i]:
                    #print(f"left is bigger than right for {left} and {right}")
                    correct_order = False
                elif left[i] < right[i]:
                    #print(f"left is smaller than right for {left} and {right}")
                    break

            if not correct_order:
                break
    except IndexError:
        # right side ran out of items, so they are not in order
        correct_order = False

    #print(f"return {correct_order} for {left} and {right}")
    return correct_order


def part1(packet_pairs):
    pair_num = 1
    pair_count = 0
    for i in range(0,len(packet_pairs),2):
        left = packet_pairs[i]
        right = packet_pairs[i+1]

        correct_order = is_correct_order(left, right)
        if correct_order:
            print(f"correct pair {pair_num}")
            pair_count += pair_num
        pair_num += 1

        print(f"compare {left} to {right} correct: {correct_order}")

    print(f"pair count {pair_count}")


def main(input_lines):
    packet_pairs = []
    for line in input_lines:
        if line:
            packet_pairs.append(json.loads(line))
    
    part1(packet_pairs)

if __name__ == "__main__":
    #input_lines = get_input("tiny_input.txt")
    input_lines = get_input()
    main(input_lines)