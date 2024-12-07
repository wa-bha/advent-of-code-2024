# Day 1: Historian Hysteria
# https://adventofcode.com/2024/day/1

def part1():
    left = []
    right = []

    # Parse data from file
    with open("day1input.txt", "r") as file:
        for line in file:
            data = line.split()
            left.append(int(data[0]))
            right.append(int(data[1]))


    # Sort both lists
    left.sort()
    right.sort()

    # Pair numbers by sorted order, ie: smallest together, then next smallest and so on
    paired = zip(left, right)

    # Calculate distance for each pair and the sum
    current_sum = 0
    for x, y in paired:
        current_sum += abs(x - y)

    return current_sum


def part2():
    left = []
    right = []

    # Parse data from file
    with open("day1input.txt", "r") as file:
        for line in file:
            data = line.split()
            left.append(int(data[0]))
            right.append(int(data[1]))

    # Build a dictionary with number (from the right list) and it's frequency
    rightCount = {}
    for x in right:
        if (x not in rightCount):
            rightCount[x] = 1
        else:
            rightCount[x] = rightCount[x] + 1
    
    # Iterate over the left list and calculate the "contribution" per number
    current_contribution = 0
    for y in left:
        if (y in rightCount):
            current_contribution += (y * rightCount[y])

    # Sum up all the contributions
    return current_contribution


print('Part 1:', part1())
print('Part 2:', part2())