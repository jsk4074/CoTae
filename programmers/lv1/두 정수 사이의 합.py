def solution(a, b):
    if a > b:
        a, b = b, a

    return sum(range(a, b + 1))

a = 3
b = 5
solution(a, b)