surrounding_mods = [
    (-1,  0), # above
    ( 0, -1), # left
]

def check_in_basins(basins, coordinates):
    print(f"      checking if {coordinates} in basins")
    for idx, basin in enumerate(basins):
        # if coordinates in basin, return index of basin
        if coordinates in basin:
            print(f"      ! in basin {idx}")
            return idx

    print(f"      ! not in any basin")
    return False

def multiply(list) :
    result = 1
    for x in list:
         result = result * x
    return result

def process(f):
    return [int(num) for num in f.strip()]

with open("input.txt") as f:
    map = list(map(process, f))

basins = []

for lidx, line in enumerate(map):
    print(f"\nI’m in line {lidx}: {line}")

    for vidx, value in enumerate(line):
        print(f"\nI’m on the value at index {vidx}: {value}")

        if value == 9:
            print("    ! skipping because I’m a 9")
            continue

        added_to_basin = False

        for lidx_mod, vidx_mod in surrounding_mods:
            comparison_lidx = lidx+lidx_mod
            comparison_vidx = vidx+vidx_mod

            if comparison_lidx < 0 or comparison_vidx < 0:
                print("    ! a comparison index is less than 0")
                continue

            try:
                comparison_value = map[comparison_lidx][comparison_vidx]
                print(f"    checking: map[{comparison_lidx}][{comparison_vidx}] -> {comparison_value}")

                if comparison_value == 9:
                    print("    ! it’s a 9")
                    continue

                # returns the index of the basin the comparison point is in
                # or returns false
                in_basin = check_in_basins(basins, (comparison_lidx, comparison_vidx))

                # if the comparision point is in a basin, add this point to
                # that basin
                if isinstance(in_basin, int):
                    basins[in_basin].add((lidx, vidx))
                    added_to_basin = True

            except:
                print(f"there is no value at line {lidx} + {lidx_mod}, value {vidx} + {vidx_mod}")
                continue

        # if this hasn’t yet been added to a basin, make a new basin with this
        # in it.
        if not added_to_basin:
            print("     -> adding a new basin")
            basins.append({(lidx, vidx)})
            print(f"    basins: {len(basins)}")

# process the basins: combine basins where there is an overlap
clean_basins = []
for idx, basin in enumerate(basins):
    if idx == 0:
        clean_basins.append(basin)
        continue

    overlap_found = False
    for cbidx, cb in enumerate(clean_basins):
        overlap = basin.intersection(cb)
        if overlap:
            print(f"\nThere is an overlap between basin {idx} and clean_basin {cbidx}: {overlap}")
            overlap_found = True
            clean_basins[cbidx] = cb.union(basin)

    if not overlap_found:
        print(f"\nThere is NO overlap between basin {idx} and other basins")
        clean_basins.append(basin)

lengths = [len(b) for b in clean_basins]
lengths.sort()
result = multiply(lengths[-3:])

print(f"\n-----------------------")
print(f"result: {result}")

# -----------------------
# result: 1075536
