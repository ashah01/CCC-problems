m = int(input())
n = int(input())
k = int(input())
grid = [[1 for _ in n] for __ in m]
for i in range(k):
    command = input().split()
    command[1] = int(command[1]) - 1
    if command == "R":
        for i in range(n):
            grid[command[1]][i] *= -1
    else:
        assert command == "C"
        for i in range(m):
            grid[i][command[1]] *= -1

gold = 0
for i in m:
    for j in n:
        if j == -1:
            gold += 1

print(gold)