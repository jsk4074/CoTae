import math 

def solution(n):
    answer = 0 
    number = math.sqrt(n)
    if number - int(number) == 0:
        return (number + 1) ** 2
    else:
        return -1

n = 121
solution(n)