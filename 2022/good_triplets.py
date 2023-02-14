n, c = list(map(int, input().split()))

points = list(map(int, input().split())) # key = index, value = value
# n, c = 8, 10
# points = [0, 2, 5, 5, 6, 9, 0, 0]

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
    
    x = a + c//2
    y: int
    bs = []
    
    if (b > c // 2):
        
        if (c_ == 0):
            c_ = c

        bs.append(b + c//2)
        bs.append(b - c // 2)
    
        if (abs(x - bs[0]) < abs(x - bs[1])):
            y = bs[0]
        
        else:
            y = bs[1]
    
    else:
        y = b + c//2
        

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
                total_triplets += 1

print(total_triplets)


# TODO: determine why some of the triplets aren't showing and why some excess are.
"""

Working: GOOD
(1, 2, 5)
(2, 3, 6)
(2, 4, 5)
(2, 5, 6)

Not working: GOOD
(2, 5, 7)
(2, 5, 8)

Excess: GOOD
(1, 5, 6)

"""