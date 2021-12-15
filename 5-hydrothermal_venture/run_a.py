from pprint import pprint

# formats data as a list of tuple pairs:
# [
#   [(0, 9), (5, 9)],
#   [(8, 0), (0, 8)],
#   [(9, 4), (3, 4)],
#   [(2, 2), (2, 1)],
#   [(7, 0), (7, 4)],
#   [(6, 4), (2, 0)],
#   [(0, 9), (2, 9)],
#   [(3, 4), (1, 4)],
#   [(0, 0), (8, 8)],
#   [(5, 5), (8, 2)]
# ]
def format_inputs(data):
    data_as_list = data.strip().split(' -> ')
    return [tuple(map(int, pair.split(","))) for pair in data_as_list]

def is_horizontal_or_vertical(pair):
    return pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]

def make_all_pairs(original_pairs):
    all_pairs = original_pairs

    x1, y1 = original_pairs[0]
    x2, y2 = original_pairs[1]

    if x1 == x2:
        print("it’s vertical")
        nums = get_numbers_between([y1, y2])
        for n in nums:
            all_pairs.append((x1, n))

    if y1 == y2:
        print("it’s horizontal")
        nums = get_numbers_between([x1, x2])
        for n in nums:
            all_pairs.append((n, y1))

    return all_pairs

def get_numbers_between(nums):
    minmax = nums
    minmax.sort()
    min, max = minmax
    r = range(min+1, max)
    return [*r]

def mark_pair(pair):
    x, y = pair

    try:
        diagram[y][x] += 1
    except IndexError:
        expand_diagram_for_pair(pair)
        mark_pair(pair)

def expand_diagram_for_pair(pair):
    x, y = pair

    while len(diagram) < y + 1:
        diagram.append([])

    for row in diagram:
        while len(row) < x + 1:
            row.append(0)

with open("input.txt") as f:
    inputs = list(map(format_inputs, f))

# [
#     [0, 0, 0, 0]
#     [0, 0, 1, 0]
#     [1, 1, 2, 0]
#     ...
# ]
diagram = []

for input in inputs:
    if not is_horizontal_or_vertical(input):
        continue

    all_pairs = make_all_pairs(input)

    for pair in all_pairs:
        mark_pair(pair)

most_dangerous_spots = 0
for row in diagram:
    for val in row:
        if val > 1:
            most_dangerous_spots += 1

print(most_dangerous_spots)

# 4745
