grid = [[1, 2], [3, 4]]
"""
Horizontal flip
[[3 4], [1, 2]]

Vertical flip
[[2, 1], [4, 3]]
"""

def horizontal(grid):
    return [grid[1], grid[0]]

def vertical(grid):
    return [[grid[0][1], grid[0][0]], [grid[1][1], grid[1][0]]]

instructions = [*input()]

for action in instructions:
    if action == "H":
        grid = horizontal(grid)
    else:
        grid = vertical(grid)

print(grid[0])
print(grid[1])