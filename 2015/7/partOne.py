circut = {}
actions = []
currentAction = ""

def circutAssign(key, value):
    try:
        circut.update({key:int(value)})
    except:
        circut.update({key:int(circut.get(value))})

def circutNot(key, value):
    try:
        circut.update({key:~int(circut.get(value))&65535})
    except:
        circut.update({key:~int(value)&65535})

def circutConnect(key, gate, var1, var2):
    first, second = 0, 0
    try:
        first = int(var1)
    except:
        first = int(circut.get(var1))

    try:
        second = int(var2)
    except:
        second = int(circut.get(var2))


    match gate:
        case "AND":
            circut.update({key:first&second})
        case "OR":
            circut.update({key:first|second})
        case "LSHIFT":
            circut.update({key:first<<second})
        case "RSHIFT":
            circut.update({key:first>>second})


def doAction(instruction):
    splitInstruction = instruction.split(" ")
    match splitInstruction.__len__():
        case 3:
            circutAssign(splitInstruction[2],splitInstruction[0])
        case 4:
            circutNot(splitInstruction[3], splitInstruction[1])
        case 5:
            circutConnect(splitInstruction[4], splitInstruction[1], splitInstruction[0],splitInstruction[2])

def runActions(booklet):
    for action in booklet.splitlines():
        try:
            actions.append(action)
            doAction(action)
            actions.remove(action)
        except:
            continue
    loop =0
    while (0==0):
        todo = actions
        for action in todo:
            try:
                doAction(action)
                actions.remove(action)
            except:
                continue
        if actions.__len__() == 0:
            break


input = open("input.txt", "r").read()

runActions(input)

print(circut.get("a"))
