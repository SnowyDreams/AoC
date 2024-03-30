def count_chars(char,index,sequence):
    count = 0
    for x in range(len(sequence) - index):
        if char == sequence[index+x]:
            count += 1
            continue
        break
    return count if count != 0 else 1

def look_and_say(sequence):
    result = ''
    x = 0
    while x < len(sequence):
        index = count_chars(sequence[x],x,sequence)
        result += f'{index}{sequence[x]}'
        if x + index >= len(sequence):
            break
        x += index
    return result

puzzle = '1113222113'
repeat = 50
output = ''

for loop in range(repeat):
    output = look_and_say(puzzle)
    puzzle = output

print(len(output))
    

