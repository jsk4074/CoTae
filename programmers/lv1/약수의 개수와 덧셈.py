def get_measure(number):
    return [i + 1 for i in range(number) if number % (i + 1) == 0]
def solution(left, right):
    result = 0 
    for i in range(left, right + 1):
        measure_list = get_measure(i)
        if len(measure_list) % 2 == 0: 
            result += i
        else:
            result -= i
    return result

left, right = 13, 17
solution(left, right)