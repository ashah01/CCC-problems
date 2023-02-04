n = int(input())
second_line = list(map(int, input().split()))
third_line = list(map(int, input().split()))

# Validation
assert len(second_line) == n + 1
assert len(third_line) == n

# Main
area = 0
for i in range(n):
    area += (second_line[i] + second_line[i+1])/2*third_line[i]

print(area)