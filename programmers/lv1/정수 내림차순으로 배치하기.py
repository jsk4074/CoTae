def solution(n):
    return int(''.join(sorted([i for i in str(n)])[::-1]))

n = 118372
solution(n) 