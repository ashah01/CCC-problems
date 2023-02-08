n,k = list(map(int, input().split()))
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

sum = 0

for i in range(n-(k-1)):
    for e in range(len(triangle[i])):
        segment = []
        for j in range(k):
            for h in range(j + 1):
                segment.append(triangle[i + j][e + h])
        
        sum += max(segment)
        print(segment)
        print(max(segment))