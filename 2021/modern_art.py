m = int(input())
n = int(input())
k = int(input())
grid = [[1 for _ in range(n)] for __ in range(m)]
grid_copy = grid
for i in range(k):
    command = input().split()
    command[1] = int(command[1]) - 1
    if command[0] == "R":
        for i in range(n):
            grid[command[1]][i] *= -1
    else:
        assert command[0] == "C"
        for i in range(m):
            grid[i][command[1]] *= -1

total = 0
for arr in grid:
    total += sum(arr)
print(int((m * n - total) / 2))