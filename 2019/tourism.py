import math
split_input = list(map(int, input().split()))
scores = list(map(int, input().split()))
n = split_input[0]
k = split_input[1]
assert len(scores) == n


def decompose_trip(num_locations, max_per_day):
    # Number of days the trip spans
    minimum_days = int(math.ceil(num_locations / max_per_day))
    possibilities = [[0] for _ in range(minimum_days)]
    remainder_days = num_locations - (int(math.floor(num_locations / max_per_day)) * max_per_day)
    for i in range(minimum_days):
        for index, array in enumerate(possibilities):
            if index == i:
                array.append(remainder_days)
            else:
                array.append(max_per_day)
    
    return possibilities



possible_trips = decompose_trip(n, k)
highest_score = 0
for trip in possible_trips:
    # [0, 2, 3, 3, 3]
    score_sum = 0
    days_elapsed = 0
    for i in range(len(trip) - 1): # [0, 1, 2, 3, 4]
        days_elapsed += trip[i]
        score_sum += max(scores[days_elapsed:days_elapsed+trip[i+1]])
    
    if score_sum > highest_score:
        highest_score = score_sum

print(highest_score)