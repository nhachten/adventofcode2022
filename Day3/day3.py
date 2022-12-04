import sys

sys.path.append("../../AoC2022")

from input_parser import get_input

def part1(input_lines):
    total = 0

    for line in input_lines:
        length = int(len(line)/2)
        comp1 = line[:length]
        comp2 = line[length:]

        for item in comp1:
            if item in comp2:
                if item.isupper():
                    val = ord(item) - 38 #ascii value normalized to 27 - 52
                else:
                    val = ord(item) - 96 #ascii value normalized to 1 - 26
                print("Found dup is {} in {} with val {}".format(item, line, val))
                total += val
                break

    print(total)

def part2(input_lines):
    total = 0
    i = 0
    while i < len(input_lines):
        elf1 = input_lines[i + 0]
        elf2 = input_lines[i + 1]
        elf3 = input_lines[i + 2]
        i += 3

        for item in elf1:
            if item in elf2 and item in elf3:
                if item.isupper():
                    val = ord(item) - 38 #ascii value normalized to 27 - 52
                else:
                    val = ord(item) - 96 #ascii value normalized to 1 - 26
                print("Found badge is {} with val {} for group {}".format(item, val, int(i/3)))
                total += val
                break
    
    print(total)

def main(input_lines):
    part2(input_lines)
    

if __name__ == "__main__":
    input_lines = get_input()
    main(input_lines)