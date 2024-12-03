# Day 2: Red-Nosed Reports
# https://adventofcode.com/2024/day/2

def part1solution():
    data = {}

    # Parse data from file
    with open("day2input.txt", "r") as file:
        for index, line in enumerate(file):
            data[index] = line.split()
    

    # Check the step rule, the difference between consecutive number must be between 1 and 3 (inclusive)
    # Check the consistency rule, all numbers either increase or decrease
    # ^ If both are true, the report is safe.

    safe = 0

    for reportLine in data.values():
        differences = []
        for i in range(len(reportLine) - 1):
            # convert the numbers into a differences array
            differences.append(int(reportLine[i]) - int(reportLine[i + 1]))
        
        # (Consistency): all positive or all negative
        if all(d >= 0 for d in differences) or all(d < 0 for d in differences):
            
            # (Step rule): all differences is < 1 or > 3, break
            if all(1 <= abs(d) <= 3 for d in differences):
                safe += 1
                
    return safe

print('Part 1 solution:', part1solution())
