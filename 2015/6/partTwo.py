import re

input = open("input.txt", "r").readlines()
size = 1000
display = []
for x in range(size):
    row=[]
    for y in range(size):
        row.append(0)
    display.append(row)

def act(coords,action):
    for x in range(coords[0],coords[2]+1):
        for y in range(coords[1],coords[3]+1):

            if action == "n":
                display[x][y] += 1
            if action == "f" and display[x][y]>0:
                display[x][y] -= 1
            if action ==  " ":
                display[x][y] += 2

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
        on += light
print(on)
