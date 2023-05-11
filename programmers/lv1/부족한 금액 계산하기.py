def solution(price, money, count):
    tmp = money - sum([i * price for i in range(count + 1)])
    if tmp >= 0:
        return 0
    else:
        return abs(tmp)

price, money, count, _ = 3, 20, 4, 10
solution(price, money, count)