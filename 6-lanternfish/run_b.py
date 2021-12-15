file = open('input.txt', 'r')
inputs = list(map(int, file.readlines()[0].strip().split(",")))

fish_counts = [0 for i in range(9)]
for i in inputs: fish_counts[i] += 1

for day in range(256):
    print(f"day {day}: {fish_counts}")

    zeros = fish_counts.pop(0)
    fish_counts.append(zeros)
    fish_counts[6] += zeros

print(f"\ncount of fish: {sum(fish_counts)}")

# count of fish: 1631629590423
