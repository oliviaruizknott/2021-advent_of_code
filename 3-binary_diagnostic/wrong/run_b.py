# NOTE: This attempt was wrong because I didn’t understand that you needed to
# find the most common digit for a bit out of the REMAINING values; I was using
# the most/least common information from the whole data set.

def strip(string):
    return string.strip()

with open("../input.txt") as f:
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

# PART 2: Find the most_common and least_common in binary
most_common = ""
least_common = ""

for val in count_of_ones:
    if val > len(inputs) / 2:
        most_common += "1"
        least_common += "0"
    else:
        most_common += "0"
        least_common += "1"

print("\nPART 2")
print(f"most_common:  {most_common}")
print(f"least_common: {least_common}")

print("\nPART 3")
oxygen_generator_rating_list = inputs.copy()
for idx, val in enumerate(most_common):
    for input in inputs:
        if not input[idx] == val:
            try:
                oxygen_generator_rating_list.remove(input)
            except ValueError:
                continue

    if len(oxygen_generator_rating_list) == 1:
        print(f"oxygen_generator_rating_list: {oxygen_generator_rating_list}")
        break

co2_scrubber_rating_list = inputs.copy()
for idx, val in enumerate(least_common):
    for input in inputs:
        if not input[idx] == val:
            try:
                co2_scrubber_rating_list.remove(input)
            except ValueError:
                continue

    if len(co2_scrubber_rating_list) == 1:
        print(f"co2_scrubber_rating_list:     {co2_scrubber_rating_list}")
        break

oxygen_generator_rating = int(oxygen_generator_rating_list[0], 2)
co2_scrubber_rating = int(co2_scrubber_rating_list[0], 2)
life_support_rating = oxygen_generator_rating*co2_scrubber_rating
print("\nPART 4")
print(f"oxygen_generator_rating: {oxygen_generator_rating}")
print(f"co2_scrubber_rating:     {co2_scrubber_rating}")
print(f"life_support_rating:     {life_support_rating}")


# FIRST ATTEMPT
# PART 1
# This is the count of 1s in each position:
# [488, 499, 497, 506, 484, 485, 490, 501, 503, 483, 493, 515]
#
# PART 2
# most_common: 000100011001
# least_common: 111011100110
#
# PART 3
# oxygen_generator_rating_list: ['000100011011']
# co2_scrubber_rating_list: ['111011100111']
#
# PART 4
# oxygen_generator_rating: 283
# co2_scrubber_rating: 3815
# result: 1079645
