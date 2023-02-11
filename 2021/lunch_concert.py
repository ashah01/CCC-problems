n = int(input())
positions = []
speeds = []
hearing_ranges = []
for i in range(n):
    friend_data = list(map(int, input().split()))
    positions.append(friend_data[0])
    speeds.append(friend_data[1])
    hearing_ranges.append(friend_data[2])

total_seconds = float("inf")
best_c = positions[0]
for c in range(min(positions), max(positions)):
    tmp = 0
    for i in range(n):
        tmp += max([0, (abs(c - positions[i]) - hearing_ranges[i])]) * speeds[i]
    if tmp < total_seconds:
        total_seconds = tmp
        best_c = c

print(total_seconds)