def solution(ingredient):
    ingredient_str = ''.join([str(i)for i in ingredient])

    count = 0 

    while 1:
        if '1231' in ingredient_str:
            ingredient_str = ingredient_str.replace('1231', '')
            count += 1
        else:
            return count
        
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]	
# 2
solution(ingredient)