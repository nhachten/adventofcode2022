import sys

sys.path.append("../../AoC2022")

from input_parser import get_input

def main(input_lines):
    elfnum = 1
    print("Elf {}", elfnum)
    current_elf_cals = 0
    most_elf_cals = 0
    elf_cals = []
    for line in input_lines:
        if not line:
            elfnum += 1
            print("Elf {}".format( elfnum))
            elf_cals.append(current_elf_cals)
            if current_elf_cals > most_elf_cals:
                most_elf_cals = current_elf_cals
            current_elf_cals = 0
        else:
            print("{}".format(line))
            current_elf_cals += int(line)

    print("The most cals: {}".format(most_elf_cals))
    elf_cals.sort()
    print("Top three are {}".format(sum(elf_cals[-3:])))
        

if __name__ == "__main__":
    input_lines = get_input()
    main(input_lines)