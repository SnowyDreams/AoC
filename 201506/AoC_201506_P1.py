import re

input = open("input.txt", "r").readlines()
size = 1000
display = []
for x in range(size):
    row=[]
    for y in range(size):
        row.append(False)
    display.append(row)

def act(coords,action):
    for x in range(coords[0],coords[2]+1):
        for y in range(coords[1],coords[3]+1):
            match action:
                case "n":
                    display[x][y] = True
                case "f":
                    display[x][y] = False
                case " ":
                    display[x][y] = not display[x][y]

for line in input:
    split = re.split(r"\D", line)
    coords = [] # [x1,y1,x2,y2]
    for num in split:
        if num != '':
            coords.append(int(num))
    act(coords,line[6])

on = 0
for row in display:
    for light in row:
        if light:
            on += 1
print(on)
