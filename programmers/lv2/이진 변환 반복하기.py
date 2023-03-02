def solution(s):
    replace_count = 0
    cycle_count = 0
    while 1: 
        if s == '1':
            return(cycle_count, replace_count)
        cycle_count += 1
        replace_count += s.count('0')

        s = s.replace('0', '')
        s = bin(len(s))[2:]

s = ["110010101001", "01110", "1111111"]
# [3, 8]	
# [3, 3]
for i in s: 
    print(solution(i))