def solution(num):
    count = 0
    while 1:
        if count == 500: 
            return -1
        if num % 2 == 0:
            num = num / 2
        elif num == 1:
            return count
        else: 
            num = (num * 3) + 1
        count += 1

# 8
solution(626331)