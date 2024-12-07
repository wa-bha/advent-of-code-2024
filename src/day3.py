# Day 3: Mull It Over
# https://adventofcode.com/2024/day/3

import re

def part1solution():
    # Parse data from file
    with open("day3input.txt", "r") as file:
        content = file.read()

        # Extract valid (x, y) tuples from matching "mul(x,y)"" substrings
        matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', content)

        # Get the product of each extracted tuple "instruction"
        return sum(int(x) * int(y) for x, y in matches)
    
def part2solution():
    # Parse data from file
    with open("day3input.txt", "r") as file:
        content = file.read()

        # find all do/don't and valid mul(x,y) matches
        matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', content)

        # starts as enabled
        is_next_instruction_valid = True
        total = 0

        for match in matches:
            if (match == "do()"):
                is_next_instruction_valid = True

            elif (match == "don't()"):
                is_next_instruction_valid = False
            
            else:
                if (is_next_instruction_valid == True):
                    tuple = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', match)
                    total += int(tuple[0][0]) * int(tuple[0][1])

        return total

print('Part 1 solution:', part1solution())
print('Part 2 solution:', part2solution())

