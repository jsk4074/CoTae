import numpy as np
def solution(arr1, arr2):
    return np.ndarray.tolist(np.add(arr1, arr2))

arr1, arr2 = [[1,2],[2,3]], [[3,4],[5,6]]	
solution(arr1, arr2)