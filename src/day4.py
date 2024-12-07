# Day 4: Ceres Search
# https://adventofcode.com/2024/day/4

directions = [
  (1, 0),  # right
  (-1, 0), # left
  (0, 1),  # down
  (0, -1), # up
  (1, 1),  # down-right
  (-1, -1),# up-left
  (1, -1), # down-left
  (-1, 1), # up-right
]

def is_valid_XMAS(row, col, direction, grid, max_rows, max_cols):
    word = "XMAS"

    # check if the word can fit in the direction from the current position
    for i in range(len(word)):
        new_row = row + i * direction[1]
        new_col = col + i * direction[0]

        # check that the new col/row is within max bounds of the grid
        if (new_row < 0 or new_row >= max_rows or new_col < 0 or new_col >= max_cols):
            return False
        
        # return false if the letter doesn't match
        if grid[new_row][new_col] != word[i]:
            return False
        
    return True

def part1():
    grid = []

    with open("day4input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    count = 0
    max_rows = len(grid)
    max_cols = len(grid[0])

    # Find the each "X"
    for row in range(max_rows):
        for col in range(max_cols):
            if grid[row][col] == 'X':

                # Check if the "X" is a valid "XMAS" in each direction
                for direction in directions:
                    if is_valid_XMAS(row, col, direction, grid, max_rows, max_cols):
                        count += 1

    return count

def part2():
    pass

print('Part 1 solution:', part1())
print('Part 2 solution:', part2())
