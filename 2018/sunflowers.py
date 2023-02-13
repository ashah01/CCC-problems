"""

Good orientation example
1 3 
2 9

Observations:
Ascending rows
Ascending columns


Task:
Rotate by 90° until good orientation is obtained
Output good orientation


Pseudocode:
1. Define good orientation validator
2. Define 90 degree rotation transformation
3. while (not grid.good_orientation()):
    grid.rotate()
"""
class Grid:
    def __init__(self, grid):
        self.grid = grid
    
    def good_orientation(self):
        smallest_index = 0
        # Validate column
        for i in self.grid:
            if i[0] >= smallest_index:
                smallest_index = i[0]
            else:
                return False
        
        # Validate row
        smallest_index = 0
        for i in self.grid[0]:
            if i >= smallest_index:
                smallest_index = i
            else:
                return False
        
        return True
    
    def rotate(self):
        length = len(self.grid)
        grid = []
        for i in range(length-1, -1, -1):
            grid.append([j[i] for j in self.grid])
        self.grid = grid
    

n = int(input())
grid = Grid([list(map(int, input().split())) for _ in range(n)])

while (not grid.good_orientation()):
    grid.rotate()

for i in grid.grid:
    for j in i:
        print(j, end=" ")
    print()