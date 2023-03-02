def solution(arr, divisor):
    div_result = [i for i in arr if i%divisor == 0]
    if div_result == []: 
        return  [-1]
    else:
        return sorted(div_result)

arr, divisor, _ = [2, 36, 1, 3], 1, [1, 2, 3, 36]
arr, divisor, _ = [3,2,6], 10, [-1]
arr, divisor, _ = [5, 9, 7, 10], 5, [5, 10]

print(_ == solution(arr, divisor))
solution(arr, divisor)