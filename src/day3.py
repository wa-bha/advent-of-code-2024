# Day 3: Mull It Over
# https://adventofcode.com/2024/day/3

import re

def part1():
    # Parse data from file
    with open("day3input.txt", "r") as file:
        content = file.read()

        # Extract valid (x, y) tuples from matching "mul(x,y)"" substrings
        matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', content)

        # Get the product of each extracted tuple "instruction"
        return sum(int(x) * int(y) for x, y in matches)
    
def part2():
    # Parse data from file
    with open("day3input.txt", "r") as file:
        content = file.read()

        # extract all "do()", "don't" and "valid mul(x,y)" matches
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
                    # put both decimal sequences into a list
                    decimals = re.findall(r'\d+', match)

                    # parse as int variables, then append to total
                    x, y = map(int, decimals)
                    total += x * y

        return total

print('Part 1:', part1())
print('Part 2:', part2())
