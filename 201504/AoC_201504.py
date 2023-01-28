import hashlib

key = "bgvyzdsv"
count = 0

while(True):
    m = hashlib.md5()
    m.update((key+str(count)).encode(encoding='UTF-8'))
    #if str(m.hexdigest()).startswith("00000"): #part one require at least 5 zeros
    if str(m.hexdigest()).startswith("000000"): #part two require at least 6 zeros
        print(count)
        break
    count+=1