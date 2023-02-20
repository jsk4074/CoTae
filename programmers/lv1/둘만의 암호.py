def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in list(skip):
        alphabet = alphabet.replace(i, '')


    incode = [alphabet.find(i) + index for i in s]

    incode_result = []
    for i in incode:
        if i >= len(alphabet):
            incode_result.append(i - len(alphabet))
        else: 
            incode_result.append(i)
    
    incode_result_result = []
    for i in incode_result:
        if i >= len(alphabet):
            incode_result_result.append(i - len(alphabet))
        else: 
            incode_result_result.append(i)
    
    return ''.join([alphabet[i] for i in incode_result_result])

s = "aukks"	
skip = "wbqd"	
index = 5	
# "happy"
solution(s, skip, index)