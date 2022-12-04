file = open("day1.input")
max_cal = []
sum = 0
for line in file:
    if line == "\n":
        max_cal.append(sum)
        sum = 0
    else:
        sum += int(line)

max_cal.sort()

print(max_cal[len(max_cal) - 1])
print(max_cal[len(max_cal) - 3] + max_cal[len(max_cal) - 2] + max_cal[len(max_cal) - 1])
