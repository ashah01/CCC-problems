# n, c = list(map(int, input().split()))

# points = list(map(int, input().split())) # key = index, value = value
n, c = 8, 10
points = [0, 2, 5, 5, 6, 9, 0, 0]

def is_good_triplet(a, b, c_):
    # Test if c/2 works on odd circumferences
    if (a == b or a == c_ or b == c_):
        return False
    
    if (period_addition(a, c//2) == b):
        return False

    if (c_ == period_addition(a, c//2)):
        return False
    
    if (c_ == period_addition(b, c//2)):
        return False
    
    x: int
    y: int
    if period_addition(a, c//2) == 0:
        x = c
    else:
        x = period_addition(a, c//2)
    
    if period_addition(b, c//2) == 0:
        y = c
    else:
        y = period_addition(b, c//2)

    if (c_ in range(min(x, y), max(x, y))):
        return True
    else:
        return False

def period_addition(point, segment):
    if (point >= segment):
        return (point + segment) - c
    else:
        return point + segment


total_triplets = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if is_good_triplet(points[i], points[j], points[k]):
                print(i + 1, j + 1, k + 1)
            #     total_triplets += 1


# TODO: determine why some of the triplets aren't showing and why some excess are.