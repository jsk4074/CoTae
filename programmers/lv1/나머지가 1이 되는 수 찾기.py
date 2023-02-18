def solution(n):
    for i in range(n):
        if i != 0 and n % i == 1:
            return i

n = 10
solution(n)