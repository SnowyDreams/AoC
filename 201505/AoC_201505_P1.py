import re

input = open("input.txt", "r").readlines()
nice = 0
for line in input:
    badS = ["ab","cd","pq","xy"]
    
    twice = False # at least one character apearing twice
    bad = False # containes one of the bad strings
    vowels = False # contain 3 or more vowels

    for sub in badS:
        if re.search(sub,line) != None:
            bad = True
            break

    for i,char in enumerate(line):
        if line[i] == line[i-1]:
            twice = True

    if len(re.findall(r"[aeiou]", line)) >= 3:
        vowels = True

    if twice and vowels and not bad:
        nice +=1

print(nice)


