import sys

sys.path.append("../../AoC2022")

from input_parser import get_input

from collections import namedtuple

Elf = namedtuple("Elf", "start end size")

def get_assig_start_end_size(elf_range):
    start = int(elf_range.split('-')[0])
    end = int(elf_range.split('-')[1])
    size = end - start + 1

    return Elf(start, end, size)

def part1(input_lines):
    total = 0
    for line in input_lines:
        elf1_range = line.split(',')[0]
        elf2_range = line.split(',')[1]

        elf1 = get_assig_start_end_size(elf1_range)
        elf2 = get_assig_start_end_size(elf2_range)

        overlap_score = 0
        if elf1.start <= elf2.start and elf1.end >= elf2.start:
            overlap_score = min(elf1.end, elf2.end) - elf2.start + 1
        elif elf2.start < elf1.start and elf2.end >= elf1.start:
            overlap_score = min(elf1.end, elf2.end) - elf1.start + 1

        print(line)
        print(overlap_score)

        # part 1
       # if overlap_score == min(elf1.size, elf2.size):
        #    print("Encompasses")
        #    total += 1
        # part 2
        if overlap_score > 0:
            print("Overlap some")
            total += 1

    return total


def main(input_lines):
    result = part1(input_lines)

    print(result)
    

if __name__ == "__main__":
    input_lines = get_input()
    main(input_lines)