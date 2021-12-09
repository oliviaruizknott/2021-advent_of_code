def process(line):
    return [tuple(input.strip().split(" ")) for input in line.split(" | ")]

lengths = (2, 3, 4, 7)
cout_of_relevant_digits = 0

with open("input.txt") as f:
    inputs = list(map(process, f))

for i in inputs:
    patterns, output = i
    for o in output:
        if len(o) in lengths: cout_of_relevant_digits += 1

print(cout_of_relevant_digits)

# 284
