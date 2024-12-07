# Day 3: Mull It Over
# https://adventofcode.com/2024/day/3

import re

def part1solution():
    # Parse data from file
    with open("day3input.txt", "r") as file:
        content = file.read()

        # Extract valid (x, y) tuples from matching "mul(x,y)"" substrings
        matches = (re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', content))

        # Get the product of each extracted tuple "instruction"
        return sum(int(x) * int(y) for x, y in matches)

print('Part 1 solution:', part1solution())

