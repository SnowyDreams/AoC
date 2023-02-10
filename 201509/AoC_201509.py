import itertools

input = open('exampleInput.txt','r').read()
input = open('input.txt','r').read()

places = [] 
placesDist = {} # Distance between a pair of places
routeDist = [] # Distance of routes

# Extract places and distances from input 
for line in input.splitlines():
    lineParts = line.split(' ')
    places.extend([lineParts[0],lineParts[2]])
    placesDist.update({f"{lineParts[0]+lineParts[2]}":lineParts[4]})

# Remove duplicates
places = [*set(places)]

# Count places
placeCount = places.__len__()

# Creates all possible routes
routes = list(itertools.permutations(places,places.__len__()))

# Checks distance of each route
for route in routes:
    
    dist = 0
    for x in range(placeCount-1):
        dist += int(placesDist[route[x]+route[x+1]]) if f"{route[x]}{route[x+1]}" in placesDist else int(placesDist[route[x+1]+route[x]])
    routeDist.append(dist)
    # print(f"{route} = {dist}")

routeDist.sort()

# print shortest distance
print(routeDist[0])