file = open('input.txt', 'r')
inputs = file.readlines()

horizontal_position = 0
depth = 0
aim = 0

for val in inputs:
    [command, num] = val.split(' ')
    num = int(num)

    if command == 'forward':
        horizontal_position += num
        depth += (aim*num)

    if command == 'up':
        aim -= num

    if command == 'down':
        aim += num

print("horizontal position: ", horizontal_position)
print("depth:               ", depth)
print("--------------------------\n")
print(horizontal_position*depth)

# horizontal position:  1823
# depth:                1012318
# --------------------------
#
# 1845455714
