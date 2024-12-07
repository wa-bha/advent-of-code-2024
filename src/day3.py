# Day 3: Mull It Over
# https://adventofcode.com/2024/day/3

import re

def part1solution():
    print('hi')

    matches = []

    # Parse data from file
    with open("day3input.txt", "r") as file:
        for line in file:

            # Extract any valid mul(x,y) substrings, and append to the array
            matches.extend(re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line))

    total = 0

    # loop through all matches
    for match in matches:
        # convert mul(x,y) to x * y, then += to total
        match = match.replace("mul(", "")
        match = match.replace(")", "")
        match = match.split(",")
        total += int(match[0]) * int(match[1])
        
    return total

print('Part 1 solution:', part1solution())
