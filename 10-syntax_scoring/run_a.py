OPENERS = ("(", "[", "{", "<",)
CLOSERS = (")", "]", "}", ">",)

tag_dict_by_closer = {
    ")": {
        "opener": "(",
        "score": 3
    },
    "]": {
        "opener": "[",
        "score": 57
    },
    "}": {
        "opener": "{",
        "score": 1197
    },
    ">": {
        "opener": "<",
        "score": 25137
    },
}

def process(input):
    return input.strip()

with open("input.txt") as f:
    inputs = list(map(process, f))

score = 0

for line in inputs:
    print(f"\nexamining line: {line}")

    openers_sequence = []
    for char in line:
        print(f"  examining character: {char}")
        if char in OPENERS:
            openers_sequence.append(char)

        if char in CLOSERS:
            if openers_sequence[-1] == tag_dict_by_closer[char]["opener"]:
                openers_sequence.pop()
                continue

            else:
                print(f"ERROR! {char} does not correspond with {openers_sequence[-1]}")
                score += tag_dict_by_closer[char]["score"]
                break

print(score)

# 344193
