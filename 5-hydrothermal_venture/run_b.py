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
    print(f"\noriginal_pairs: {original_pairs}")
    all_pairs = original_pairs

    new_coordinates = []

    for idx in range(len(original_pairs[0])):
        print(f"index: {idx}")

        original_numbers = [pair[idx] for pair in original_pairs]
        print(f"original_numbers: {original_numbers}")

        numbers_between = get_numbers_between([pair[idx] for pair in original_pairs])
        print(f"numbers_between: {numbers_between}")

        new_coordinates.append(numbers_between)

    while len(new_coordinates[0]) < len(new_coordinates[1]):
        new_coordinates[0].append(original_pairs[0][0])

    while len(new_coordinates[1]) < len(new_coordinates[0]):
        new_coordinates[1].append(original_pairs[0][1])

    new_pairs = list(zip(new_coordinates[0], new_coordinates[1]))

    return original_pairs + new_pairs

def get_numbers_between(nums):
    minmax = nums.copy()
    minmax.sort()
    min, max = minmax

    as_range = range(min+1, max)
    numbers_in_list = [*as_range]

    if not nums == minmax:
        numbers_in_list.reverse()

    return numbers_in_list

def expand_diagram_for_pair(pair):
    x, y = pair

    while len(diagram) < y + 1:
        diagram.append([])

    for row in diagram:
        while len(row) < x + 1:
            row.append(0)

def mark_pair(pair):
    x, y = pair

    try:
        diagram[y][x] += 1
    except IndexError:
        expand_diagram_for_pair(pair)
        mark_pair(pair)

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
    all_pairs = make_all_pairs(input)

    for pair in all_pairs:
        mark_pair(pair)

most_dangerous_spots = 0
for row in diagram:
    for val in row:
        if val > 1:
            most_dangerous_spots += 1

print(f"\nMOST DANGEROUS SPOTS: {most_dangerous_spots}")

# MOST DANGEROUS SPOTS: 18442
