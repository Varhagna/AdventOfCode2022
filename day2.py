def encode(string):
    string = string.replace("A", "1")
    string = string.replace("B", "2")
    string = string.replace("C", "3")
    return int(string)


def choice(you, opp):
    if you == "Y":
        return opp
    elif you == "X":
        if opp == "A":
            return "C"
        elif opp == "B":
            return "A"
        else:
            return "B"
    else:
        if opp == "A":
            return "B"
        elif opp == "B":
            return "C"
        else:
            return "A"


def win(you, opp):
    if you == "A" and opp == "C":
        return True
    elif you == "C" and opp == "B":
        return True
    elif you == "B" and opp == "A":
        return True
    else:
        return False


file = open("day2.input")
data1 = []
data2 = []
score = 0
for line in file:
    arr = line.split("\n")[0].split(" ")
    opp = arr[0]
    you = choice(arr[1], opp)
    if you == opp:
        score += 3 + encode(you)
    elif win(you, opp):
        score += 6 + encode(you)
    else:
        score += 0 + encode(you)

print(score)
