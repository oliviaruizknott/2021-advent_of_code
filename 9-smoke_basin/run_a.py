surrounding_points = [
              (-1, 0),
    ( 0, -1),          ( 0, 1),
              ( 1, 0),
]

def process(f):
    return [int(num) for num in f.strip()]

with open("input.txt") as f:
    map = list(map(process, f))

low_points = []
for lidx, line in enumerate(map):
    print(f"\nI’m in line {lidx}: {line}")

    for vidx, value in enumerate(line):
        print(f"\nI’m on the value at index {vidx}: {value}")

        lower_than_surrounding = True
        for lidx_mod, vidx_mod in surrounding_points:
            comparison_lidx = lidx+lidx_mod
            comparison_vidx = vidx+vidx_mod

            if comparison_lidx < 0 or comparison_vidx < 0:
                print("    ! a comparison index is less than 0")
                continue

            try:
                comparison_value = map[comparison_lidx][comparison_vidx]
                print(f"    comparing to: map[{comparison_lidx}][{comparison_vidx}] -> {comparison_value}")

                if value >= comparison_value:
                    print(f"    ! value {value} is higher than {comparison_value}")
                    lower_than_surrounding = False
                    break

            except:
                print(f"there is no value at line {lidx} + {lidx_mod}, value {vidx} + {vidx_mod}")
                continue

        if lower_than_surrounding:
            low_points.append(value)

print(f"\n-----------------------")
print(f"low points: {low_points}")
print(f"risk level: {sum([point+1 for point in low_points])}")

# FIRST ATTEMPT
#
# low points: [3, 0, 1, 0, 0, 1, 1, 0, 0, 0, 2, 1, 1, 1, 2, 1, 0, 0, 4, 1, 2, 0, 3, 0, 4, 3, 0, 1, 2, 2, 3, 0, 0, 4, 0, 1, 3, 2, 2, 0, 0, 2, 2, 1, 3, 5, 0, 0, 0, 3, 2, 1, 1, 0, 2, 0, 1, 4, 3, 0, 0, 4, 1, 0, 1, 0, 1, 0, 1, 0, 4, 2, 1, 0, 0, 3, 0, 0, 0, 4, 1, 0, 2, 0, 0, 0, 3, 4, 0, 2, 3, 2, 0, 0, 0, 1, 0, 4, 0, 2, 0, 0, 0, 3, 0, 0, 1, 1, 0, 4, 0, 0, 0, 3, 0, 0, 3, 0, 3, 0, 2, 0, 0, 0, 0, 0, 1, 1, 6, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 2, 0, 1, 1, 4, 1, 0, 5, 1, 0, 2, 0, 1, 0, 3, 1, 3, 0, 0, 4, 0, 1, 5, 4, 1, 0, 1, 1, 2, 1, 2, 0, 1, 2, 2, 0, 6, 0, 2, 0, 0, 5, 5, 0, 3, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1, 2, 0, 0, 0, 2, 1, 2, 0, 0, 0, 3, 3, 1, 2, 1, 1, 0, 0, 0, 0, 2, 3, 0, 1, 1, 0]
# risk level: 485
#
# -> too low

# SECOND ATTEMPT
#
# low points: [2, 2, 3, 0, 1, 0, 0, 1, 1, 0, 0, 0, 2, 1, 1, 1, 2, 1, 0, 0, 4, 1, 2, 0, 3, 0, 4, 3, 0, 1, 2, 2, 3, 0, 0, 4, 0, 1, 3, 2, 2, 0, 0, 2, 2, 1, 3, 5, 0, 0, 0, 3, 2, 1, 1, 0, 2, 0, 1, 4, 3, 0, 0, 4, 1, 0, 1, 0, 1, 0, 1, 0, 4, 2, 1, 0, 0, 3, 0, 0, 0, 4, 1, 0, 2, 0, 0, 0, 3, 4, 0, 2, 3, 2, 0, 0, 0, 1, 0, 4, 0, 2, 0, 0, 0, 3, 0, 0, 1, 1, 0, 4, 0, 0, 0, 3, 0, 0, 3, 0, 3, 0, 2, 0, 0, 0, 0, 0, 1, 1, 6, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 2, 0, 1, 1, 4, 1, 0, 5, 1, 0, 2, 0, 1, 0, 3, 1, 3, 0, 0, 4, 0, 1, 5, 4, 1, 0, 1, 1, 2, 1, 2, 0, 1, 2, 2, 0, 6, 0, 2, 0, 0, 5, 5, 0, 3, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1, 2, 0, 0, 0, 2, 1, 2, 0, 0, 0, 3, 3, 1, 2, 1, 1, 0, 0, 0, 0, 2, 3, 0, 1, 1, 0]
# risk level: 491

# print(f"""
# {map[lidx-1][vidx-1]}{map[lidx-1][vidx]}{map[lidx-1][vidx+1]}
# {line[vidx-1]}{value}{line[vidx+1]}
# {map[lidx+1][vidx-1]}{map[lidx+1][vidx]}{map[lidx+1][vidx+1]}
# """)
