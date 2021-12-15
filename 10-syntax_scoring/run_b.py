OPENERS = ("(", "[", "{", "<",)
CLOSERS = (")", "]", "}", ">",)
pairs_by_opener = dict(zip(OPENERS, CLOSERS))
pairs_by_closer = dict(zip(CLOSERS, OPENERS))
points_by_closer = dict(zip(CLOSERS, range(1,5)))

def process(input):
    return input.strip()

def get_points_for_sequence(sequence):
    total = 0
    for char in sequence:
        total = total * 5
        total += points_by_closer[char]

    return total

with open("input.txt") as f:
    inputs = list(map(process, f))

incomplete_lines = []

for line in inputs:
    print(f"\nexamining line: {line}")

    corrupt_line = False
    openers_sequence = []
    for char in line:
        print(f"  examining character: {char}")
        if char in OPENERS:
            openers_sequence.append(char)

        if char in CLOSERS:
            if openers_sequence[-1] == pairs_by_closer[char]:
                openers_sequence.pop()
                continue

            else:
                print(f"ERROR! {char} does not correspond with {openers_sequence[-1]}")
                corrupt_line = True
                break

    if not corrupt_line:
        incomplete_lines.append(openers_sequence)

all_points = []
for line in incomplete_lines:
    sequence_to_complete = [pairs_by_opener[char] for char in line[::-1] if char not in CLOSERS]
    all_points.append(get_points_for_sequence(sequence_to_complete))

all_points.sort()
print(f"\nTOTAL POINTS: {all_points[int((len(all_points)-1)/2)]}")

# TOTAL POINTS: 3241238967
