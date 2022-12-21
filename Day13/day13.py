import sys

sys.path.append("../../AoC2022")

from input_parser import get_input

import json

def is_correct_order(left, right):
    print(f"is_correct_order {left} <<>> {right}")
    correct_order = None
    try:
        for i in range(len(left)):
            #print(f"compare {left[i]} to {right[i]}")
            if isinstance(left[i],list) or isinstance(right[i],list):
                #if not isinstance(left[i],list):
                if isinstance(left[i],int):
                    correct_order = is_correct_order([left[i]], right[i])
                #elif not isinstance(right[i],list):
                elif len(left[i]) == 0 and len(right[i]) > 0:
                    print("left len is 0")
                    correct_order = True
                elif isinstance(right[i],int):
                    correct_order = is_correct_order(left[i], [right[i]])
                else:
                    correct_order = is_correct_order(left[i], right[i])
            else:
                if left[i] > right[i]:
                    #print(f"left is bigger than right for {left} and {right}")
                    correct_order = False
                elif left[i] < right[i]:
                    #print(f"left is smaller than right for {left} and {right}")
                    correct_order = True
                #else:
                #    print("keep checking")

            if correct_order is not None:
                break
    #except IndexError or TypeError:
    except:
        # right side ran out of items, so they are not in order
        #print(f"right ran out of space")
        correct_order = False

    #print(f"return {correct_order} for {left} and {right}")
    return correct_order


def part1(packet_pairs):
    pair_num = 1
    pair_count = 0
    #n = 0
    #for i in [4]:
    #    print(f"pair number {i}")
    for i in range(0,len(packet_pairs),2):
    #for i in range(290,291):
        #n += 1
        left = packet_pairs[i]
        right = packet_pairs[i+1]

        correct_order = is_correct_order(left, right)
        if correct_order:
            #print(f"correct pair {pair_num}")
            pair_count += pair_num

        #if correct_order:
        #    print(f"{i} {pair_num} compare {left} to {right} correct: {correct_order}")
        print(f"{i} pair_num: {pair_num} - {correct_order}")
        pair_num += 1

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