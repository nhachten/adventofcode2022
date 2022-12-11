import sys
from collections import namedtuple
from pprint import pprint

sys.path.append("../../AoC2022")

from input_parser import get_input

CPUSnapshot = namedtuple("CPUSnapshot", "cycle reg_x")

def main(input_lines):
    cur_cycle = 0
    reg_x_val = 1
    cycle_reg_hist = []

    display = []
    draw_display = lambda: display.append("#") if abs(reg_x_val - (cur_cycle%40)) <= 1 else display.append(".")

    for line in input_lines:
        cycle_reg_hist.append(CPUSnapshot(cur_cycle, reg_x_val))

        inst = line.split(' ') 
        if inst[0] == "addx":
            draw_display()
            cur_cycle += 1
            draw_display()
            cur_cycle += 1
            reg_x_val += int(inst[1])
        elif inst[0] == "noop":
            draw_display()
            cur_cycle += 1


    ssi_cycle = 20
    cur_sig_strength = 0
    total_sig_strength = 0
    for i in range(len(cycle_reg_hist)):
        update_ssi_cycle = False
        if cycle_reg_hist[i].cycle >= ssi_cycle:
            cur_sig_strength = ssi_cycle * cycle_reg_hist[i-1].reg_x
            total_sig_strength += cur_sig_strength
            update_ssi_cycle = True
        if update_ssi_cycle:
            ssi_cycle += 40

        if ssi_cycle > 220:
            break

    print(total_sig_strength)
    for row in range(6):
        print(''.join(display[row*40:row*40+40]))

if __name__ == "__main__":
    input_lines = get_input()
    main(input_lines)