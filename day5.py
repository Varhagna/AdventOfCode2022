file = open("day5.input")

stacks = [[], [], [], [], [], [], [], [], []]
instr_mode = False
for line in file:
    if line.find("1") != -1 and instr_mode == False:
        instr_mode = True
        continue

    if line == "\n":
        for i in range(0, 9):
            stacks[i].reverse()
        continue

    if instr_mode:
        amount = int(line.split(" ")[1])
        src = int(line.split(" ")[3])
        dest = int(line.split(" ")[5])
        print("Amount %s, Dest %s, Src %s" % (amount, dest, src))
        for i in range(0, amount):
            ## part 1 // stacks[dest - 1].append(stacks[src - 1].pop()
            stacks[dest - 1].append(stacks[src - 1].pop(len(stacks[src - 1]) - amount + i))
    else:
        index = 1
        while len(line) > index:
            if line[index] != " ":
                stacks[int(index / 4)].append(line[index])
            index += 4


for i in range(0, 9):
    while len(stacks[i]) > 0:
        print(stacks[i].pop(0), sep=" ", end=" ")
    print()
