# Day 2: Red-Nosed Reports
# https://adventofcode.com/2024/day/2

def part1():
    safe = 0

    # Parse data from file
    with open("day2input.txt", "r") as file:
        for line in file:
            report = [int(num) for num in line.split()]

            # Calculate the difference between consecutive
            differences = [report[i] - report[i + 1] for i in range(len(report) - 1)]
        
            # Check if all differences are consistently positive or negative
            is_consistent = all(d >= 0 for d in differences) or all(d < 0 for d in differences)

            # Check if all differences between are between 1 and 3 (inclusive)
            is_step_valid = all(1 <= abs(d) <= 3 for d in differences)

            # ^ If both are true, the report is safe.
            if is_consistent and is_step_valid:
                safe += 1

    return safe

print('Part 1:', part1())
