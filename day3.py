def getDuplicate(first, second):
    for i in first:
        for j in second:
            if i == j:
                return i


def getDuplicate(first, second, third):
    for i in first:
        for j in second:
            for k in third:
                if i == j and j == k:
                    return i


def getPriority(string):
    priority = 0
    if string.isupper():
        priority += 26

    priority += ord(string.lower()) - 96
    return priority


file = open("day3.input")
sum = 0

## part 1
## for line in file:
##    first = line[: len(line) // 2]
##    second = line[len(line) // 2 :]

##    duplicate = getDuplicate(first, second)
##    sum += getPriority(duplicate)

group_cnt = 0
bag_array = []
for line in file:
    bag_array.append(line)
    group_cnt += 1
    if group_cnt == 3:
        item = getDuplicate(bag_array[0], bag_array[1], bag_array[2])
        group_cnt = 0
        sum += getPriority(item)
        bag_array = []

print(sum)
