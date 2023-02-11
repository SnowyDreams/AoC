exampleInput = '1211'
puzzleInput = '1113222113'
repeat = 1
result = ''

result = exampleInput
for x in range(repeat):
    manipulated = ''
    lastDig = ''
    count = 0
    for i in range(0,result.__len__()+1):
        if i == result.__len__():
            count = 1 if count == 0 else count
            lastDig = result[i-1]
            manipulated += f'{str(count)}{lastDig}'
            continue

        if lastDig == '':
            lastDig = result[i-1] if i-1 > 0 else result[i]

        if result[i] == lastDig:
            count += 1
        
        if result[i] != lastDig:
            manipulated += f'{str(count)}{lastDig}'
            count = 0
            continue
        # manipulated += f'{str(count)}{lastDig}'
    print(manipulated)


    