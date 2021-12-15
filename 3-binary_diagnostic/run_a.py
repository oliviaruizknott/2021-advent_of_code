def strip(string):
    return string.strip()

with open("input.txt") as f:
    inputs = list(map(strip, f))

# make a list full of 0s as long as the length of the inputs to increment as we
# loop through the inputs. it will look something like:
#
#   [0, 0, 0, 0, 0, 0, 0]
#
# --depending the length of the inputs.
# (this assumes all inputs are the same length as the first input.)
count_of_ones = [0 for i in inputs[0]]

# PART 1: Loop through the inputs and count the ones in each position
for input in inputs:
    # for each bit, increment the count in that position of the count_of_ones
    # if the bit is a 1
    for idx, val in enumerate(input):
        if val == '1':
            count_of_ones[idx] += 1

print("PART 1")
print("This is the count of 1s in each position:")
print(count_of_ones)

# PART 2: Find the gamma_rate and epsilon_rate in binary
gamma_rate = ""
epsilon_rate = ""

for val in count_of_ones:
    if val > len(inputs) / 2:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print("\nPART 2")
print(f"gamma_rate: {gamma_rate}")
print(f"epsilon_rate: {epsilon_rate}")

# PART 3: Decimal and multiply!
result = int(gamma_rate, 2) * int(epsilon_rate, 2)

print("\nPART 3")
print(f"gamma_rate in decimal: {int(gamma_rate,2)}")
print(f"epsilon_rate in decimal: {int(epsilon_rate,2)}")
print(f"result: {result}")

# PART 1
# This is the count of 1s in each position:
# [488, 499, 497, 506, 484, 485, 490, 501, 503, 483, 493, 515]
#
# PART 2
# gamma_rate: 000100011001
# epsilon_rate: 111011100110
#
# PART 3
# gamma_rate in decimal: 281
# epsilon_rate in decimal: 3814
# result: 1071734
