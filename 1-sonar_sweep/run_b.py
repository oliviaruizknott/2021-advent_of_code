file = open('input.txt', 'r')
inputs = file.readlines()

increases = 0
for idx, val in enumerate(inputs):
    if idx < 1:
        continue

    try:
        a = int(inputs[idx-1])
        b = int(inputs[idx])
        c = int(inputs[idx+1])
        d = int(inputs[idx+2])

        prev_window = a + b + c
        this_window = b + c + d

        if this_window > prev_window:
            increases += 1

    except IndexError:
        break

print(increases)

# 1518
