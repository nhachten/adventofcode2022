import sys
import re

sys.path.append("../../AoC2022")

from collections import namedtuple

from input_parser import get_input

ItemFactor = namedtuple("ItemFactor", "factor rem")

# get all the divisors
with open("input.txt", 'r') as f:
    txt = f.read()

FACTORS = list(map(int, re.findall("divisible\s{1}by\s{1}(\d+)", txt)))

class Monkey:

    def __init__(self, id, item_list, operation, test, true_case, false_case):
        self.id = id
        self.item_factor_list = []
        self.convert_item_list(item_list)
        self.operation = operation # TODO convert to namedtuple
        self.test = test
        self.true_case = true_case
        self.false_case = false_case
        self.inspection_count = 0

    def convert_item_list(self, item_list):
        for item in item_list:
            item_factors = {}
            for factor in FACTORS:
                mod = item % factor
                item_factors[factor] = mod

            self.item_factor_list.append(item_factors)

    def process_move(self, monkey_friends):
        while self.item_factor_list:
            new_item = self.inspect_item(self.item_factor_list[0])
            self.item_factor_list = self.item_factor_list[1:]
            self.throw_item(new_item, monkey_friends)

    def inspect_item(self, item_factors):
        new_table = {}
        for factor, rem in item_factors.items():
            a = rem if self.operation[0] == 'old' else int(self.operation[0])
            b = rem if self.operation[2] == 'old' else int(self.operation[2])

            if self.operation[1] == '*':
                result = a * b
            elif self.operation[1] == '+':
                result = a + b

            result %= factor
            new_table[factor] = result

        self.inspection_count += 1
        return new_table

    def catch_item(self, item):
        self.item_factor_list.append(item)

    def throw_item(self, item, monkey_friends):
        if item[self.test] == 0:
            monkey_friends[self.true_case].catch_item(item)
        else:
            monkey_friends[self.false_case].catch_item(item)
        

def main(input_lines):
    monkey_table = []

    for i in range(len(input_lines)):
        if input_lines[i].startswith("Monkey"):
            id = input_lines[i].split(' ')[1][:-1]
            item_list = [int(n) for n in input_lines[i+1].split("Starting items: ")[1].split(',')]
            op = input_lines[i+2].split("Operation: new = ")[1].split(' ')
            test = int(input_lines[i+3].split("Test: divisible by ")[1])
            true_case = int(input_lines[i+4].split("If true: throw to monkey ")[1])
            false_case = int(input_lines[i+5].split("If false: throw to monkey ")[1])
            monkey_table.append(Monkey(id, item_list, op, test, true_case, false_case))

    for round in range(10000):
        for monkey in monkey_table:
            monkey.process_move(monkey_table)
    
    inspection_counts = []
    for monkey in monkey_table:
        print(f"Monkey {monkey.id}: {monkey.item_factor_list} w/ {monkey.inspection_count} inspections")
        inspection_counts.append(monkey.inspection_count)

    inspection_counts.sort()
    top_score = inspection_counts[-1] * inspection_counts[-2]
    print(top_score)

if __name__ == "__main__":
    input_lines = get_input()
    main(input_lines)

