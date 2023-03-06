def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:      
        arr.pop(arr.index(min(arr)))   
        return arr

arr, _ = [4,3,2,1], [4,3,2]
print(solution(arr) == _)
solution(arr)