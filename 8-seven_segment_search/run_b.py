def alphebetize(input):
    return ''.join(sorted(input))

def process(line):
    return [tuple(map(alphebetize, input.strip().split(" "))) for input in line.split(" | ")]

def contains(pattern1, pattern2):
    return all([letter in pattern1 for letter in pattern2])

def get_digit_key(patterns):
    pattern_list = list(patterns)
    key = {}

    # 1 is the pattern with length of 2
    key[1] = [x for x in pattern_list if len(x) == 2][0]
    pattern_list.remove(key[1])

    # 4 is the pattern with length of 4
    key[4] = [x for x in pattern_list if len(x) == 4][0]
    pattern_list.remove(key[4])

    # 7 is the pattern with length of 3
    key[7] = [x for x in pattern_list if len(x) == 3][0]
    pattern_list.remove(key[7])

    # 8 is the pattern with length of 7
    key[8] = [x for x in pattern_list if len(x) == 7][0]
    pattern_list.remove(key[8])

    # find all the patterns with a length of 6
    six_lengths = [x for x in pattern_list if len(x) == 6]

    # 9 is the six-digit pattern that contains a 4
    key[9] = [x for x in six_lengths if contains(x, key[4])][0]
    pattern_list.remove(key[9])
    six_lengths.remove(key[9])

    # 0 is the (remaining) six-digit pattern that contains a 1
    key[0] = [x for x in six_lengths if contains(x, key[1])][0]
    pattern_list.remove(key[0])
    six_lengths.remove(key[0])

    # 6 is the only six-digit pattern left
    key[6] = six_lengths[0]
    pattern_list.remove(key[6])
    six_lengths.remove(key[6])

    # the 3 is the remaining (5-digit) pattern with a 1 in it
    key[3] = [x for x in pattern_list if contains(x, key[1])][0]
    pattern_list.remove(key[3])

    # figure out what letter is in the top right, the difference between 6 and 8
    top_right_segment = [letter for letter in key[8] if letter not in key[6]][0]

    # 2 is the remaining pattern with the top right segment in it
    key[2] = [x for x in pattern_list if top_right_segment in x][0]
    pattern_list.remove(key[2])

    # 5 is the only remaining letter
    key[5] = pattern_list[0]

    # retun a list where each pattern is at its corresponding index
    return [key[i] for i in sorted(key)]

with open("input.txt") as f:
    inputs = list(map(process, f))

final_digits = []
for i in inputs:
    patterns, output = i
    key = get_digit_key(patterns)

    digits = []
    for o in output:
        digits.append(key.index(o))

    final_digits.append(int(''.join(map(str, digits))))

print(sum(final_digits))

# 973499
