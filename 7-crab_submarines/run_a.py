file = open('input.txt', 'r')
positions = list(map(int, file.readlines()[0].strip().split(",")))

fuel_possibilities = []
for i in range(max(positions)):
    fuel = sum([abs(position - i) for position in positions])
    print(i, fuel)
    fuel_possibilities.append(fuel)

print(f"\nlowest fuel: {min(fuel_possibilities)}")

# lowest fuel: 359648
