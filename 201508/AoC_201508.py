input = open("input.txt","r").read()
literalLength = 0
memoryLength = 0

for line in input.splitlines():
    inLiteral = line.__len__()
    inMemory = eval(line).__len__()
    literalLength += inLiteral
    memoryLength += inMemory
    # print(f"{line} is {inLiteral} in literal and {inMemory} in memory")

print(literalLength-memoryLength)

