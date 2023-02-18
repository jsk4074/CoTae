def solution(x, n):
    add = x
    sol_list = []
    for i in range(n):
        sol_list.append(x)
        x += add
    return sol_list

x = 4
n = 3
solution(x, n)