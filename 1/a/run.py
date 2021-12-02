file = open('input.txt', 'r')
inputs = file.readlines()

increases = 0
for idx, val in enumerate(inputs):
    if (idx > 0) and (int(val) > int(inputs[idx-1])):
        increases += 1

print(increases)

# 1482
