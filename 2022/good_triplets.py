n, c = list(map(int, input().split()))

points = list(map(int, input().split())) # key = index, value = value

def is_good_triplet(a, b, c_):
    # Test if c/2 works on odd circumferences
    if (period_addition(a, c//2) == b):
        return False

    if (c_ == period_addition(a, c//2)):
        return False
    
    if (c_ == period_addition(b, c//2)):
        return False
    
    if (c_ in range(period_addition(a, c//2), period_addition(b, c//2))):
        return True
    else:
        return False

def period_addition(point, segment):
    if (point >= segment):
        return (point + segment) - 12
    else:
        return point + segment


total_triplets = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(i+2, n):
            total_triplets += 1
            if total_triplets == 3:
                print(points[i], points[j], points[k])
                print(is_good_triplet(points[i], points[j], points[k])) # INSIGHT: is_good_triplet works with the proper values passed in.
                break
        break
    break

# TODO: Ensure triplets with duplicate values are false in validator (2022/good_triplets.py:5)