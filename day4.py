def get_outer_inner(interval1, interval2):
    if interval1[1] - interval1[0] >= interval2[1] - interval2[0]:
        return interval1, interval2
    else:
        return interval2, interval1


file = open("day4.input")
part1_count = 0
part2_count = 0
for line in file:
    pair_arr = line.split(",")
    interval1 = pair_arr[0].split("-")
    interval2 = pair_arr[1].split("\n")[0].split("-")

    outer, inner = get_outer_inner((int(interval1[0]), int(interval1[1])), (int(interval2[0]), int(interval2[1])))

    if outer[0] <= inner[0] and inner[1] <= outer[1]:
        part1_count += 1

    if inner[0] <= outer[1] and outer[0] <= inner[1]:
        part2_count += 1

print("Part1: %s Part2: %s" % (part1_count, part2_count))
