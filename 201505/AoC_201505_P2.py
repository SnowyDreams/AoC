import re

input = open("input.txt", "r").readlines()
nice = 0
for line in input:
    noOverlap = False
    repeatWithGap = False
    x=0
    while x < len(line):
        if x < len(line) -1:
            this = [index.start() for index in re.finditer(rf"{line[x]}{line[x+1]}", line)]
            if len(this) >= 2:
                y=0
                while y < len(this)-1:
                    if this[y+1] - this[y] >=2:
                        noOverlap = True
                        break
                    y +=1
        if x < len(line) -2:
            if line[x] == line[x+2]:
                repeatWithGap= True
        x += 1

    if noOverlap and repeatWithGap:
        nice +=1

print(nice)
