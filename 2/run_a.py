file = open('input.txt', 'r')
inputs = file.readlines()

horizontal_position = 0
depth = 0

for val in inputs:
    [command, num] = val.split(' ')
    num = int(num)

    if command == 'forward':
        horizontal_position += num
    if command == 'up':
        depth -= num
    if command == 'down':
        depth += num

print("horizontal position: ", horizontal_position)
print("depth:               ", depth)
print("--------------------------\n")
print(horizontal_position*depth)

# horizontal position:  1823
# depth:                1018
# --------------------------
#
# 1855814
