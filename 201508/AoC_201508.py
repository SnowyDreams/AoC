input = open("input.txt","r").read()
# input = open("test_input.txt","r").read()

escapes = ['\x22','\x5C']
literalLength = 0
memoryLength = 0
rencodedLength = 0

def rencode(line):
    rencoded = []
    for char in line:
        if char in escapes:
            rencoded.append('\x5C')
            rencoded.append(char)
        else:
            rencoded.append(char)
    return("".join(rencoded).__len__())

for line in input.splitlines():
    inLiteral = line.__len__()
    inMemory = eval(line).__len__()
    rencoded = int(rencode(line)) +2
    literalLength += inLiteral
    memoryLength += inMemory
    rencodedLength += rencoded
    # print(f"{line} is {inLiteral} in literal and {inMemory} in memory and {rencoded} when re-encoded")

print(f"Solution for first part is: {literalLength-memoryLength}")
print(f"Solution for second part is: {rencodedLength-literalLength}")

