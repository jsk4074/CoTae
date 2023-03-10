def solution(numbers):
    list_all = list(range(10))
    return sum([i for i in list_all if numbers.count(i) == 0])

numbers, _ = [1,2,3,4,6,7,8,0], 14
solution(numbers)