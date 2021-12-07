file = open('input.txt', 'r')
positions = list(map(int, file.readlines()[0].strip().split(",")))

result = min([sum([sum(range(abs(current - proposed)+1)) for current in positions]) for proposed in range(max(positions))])
print(result)

# 100727924

# # (Slightly clearer)
#
# fuel_possibilities = []
# for proposed in range(max(positions)):
#     fuel = sum([sum(range(abs(current - proposed)+1)) for current in positions])
#     print(proposed, fuel)
#     fuel_possibilities.append(fuel)
#
# print(f"\nlowest fuel: {min(fuel_possibilities)}")
#
# # lowest fuel: 100727924
