n = int(input())
villages = []
for _ in range(n):
    villages.append(int(input()))

villages.sort()

smallest_size = float("inf")

for pos in range(1, n-1): # Iterate through each middle element
    sizel = (villages[pos] - villages[pos-1])/2
    sizer = (villages[pos+1] - villages[pos])/2
    if (sizel + sizer) < smallest_size:
        smallest_size = sizel + sizer

print(smallest_size)