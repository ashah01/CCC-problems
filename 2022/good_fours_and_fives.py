num = int(input())
solutions = 0
while num >= 0:
    if (num % 5) == 0:
        solutions += 1
    num -= 4
print(solutions)