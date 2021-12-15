from collections import Counter

def strip(string):
    return string.strip()

with open("input.txt") as f:
    starting_inputs = list(map(strip, f))

input_length = len(starting_inputs[0])

# inputs (list) : the inputs to be evaluated
# position (int): the position of each input to be evaluated
# most (bool)   : whether we are looking for the most (True) or least (False)
#                 common value
# default (string): what to return in case of a tie
def common_at_position(inputs, position, most=True, default='1'):
    all_at_position = [input[position] for input in inputs]
    counter = Counter(all_at_position)

    if counter['0'] == counter['1']:
        return default

    if not most:
        # return the least common element
        return counter.most_common()[-1][0]

    return counter.most_common(1)[0][0]

def find_rating(most=True, default='1'):
    remaining_inputs = starting_inputs.copy()
    for idx in range(input_length):
        desired_bit = common_at_position(remaining_inputs, idx, most, default)

        for val in starting_inputs:
            if not val[idx] == desired_bit:
                try:
                    remaining_inputs.remove(val)
                except ValueError:
                    continue

    return remaining_inputs[0]

oxygen_generator_rating = find_rating(True, '1')
co2_scrubber_rating = find_rating(False, '0')

print("BINARY")
print(f"oxygen_generator_rating: {oxygen_generator_rating}")
print(f"co2_scrubber_rating:     {co2_scrubber_rating}")

oxygen_generator_rating = int(oxygen_generator_rating,2)
co2_scrubber_rating = int(co2_scrubber_rating, 2)

print("\nDECIMAL")
print(f"oxygen_generator_rating: {oxygen_generator_rating}")
print(f"co2_scrubber_rating:     {co2_scrubber_rating}")

life_support_rating = oxygen_generator_rating*co2_scrubber_rating

print(f"\nlife_support_rating: {life_support_rating}")

# BINARY
# oxygen_generator_rating: 011010001111
# co2_scrubber_rating:     111001000000
#
# DECIMAL
# oxygen_generator_rating: 1679
# co2_scrubber_rating:     3648
#
# life_support_rating: 6124992
