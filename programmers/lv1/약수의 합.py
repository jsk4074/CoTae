def solution(n):
    return sum([i for i in range(n) if i != 0 and n % i == 0]) + n