n = int(input())

def is_prime(integer):
    for i in range(2, integer//2 + 1):
        if (integer % i) == 0:
            return False
    return True

averages = [int(input()) for _ in range(n)]

for average in averages:
    for i in range(average, 2, -1):
        lower = is_prime(i)
        if lower:
            higher = is_prime((average-i) + average)
            if higher:
                print((average-i) + average, i)
                break


