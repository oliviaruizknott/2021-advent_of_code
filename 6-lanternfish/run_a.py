file = open('input.txt', 'r')
inputs = list(map(int, file.readlines()[0].strip().split(",")))

days = 80
fishes = inputs.copy()

for idx, day in enumerate(range(days+1)):
    print(f"day {idx}: {len(fishes)}")
    fish_to_add = 0
    for fidx, fish in enumerate(fishes):
        if fish > 0:
            fishes[fidx] -= 1
        if fish == 0:
            fishes[fidx] = 6
            fish_to_add += 1

    if not idx == days:
        [fishes.append(8) for fta in range(fish_to_add)]
        fish_to_add = 0

print(f"count of fish: {len(fishes)}")

# count of fish: 360610
