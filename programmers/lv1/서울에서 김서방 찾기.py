def solution(seoul):
    count = 0
    for i in seoul:
        if i == 'Kim':
            return "김서방은 " + str(count) + "에 있다"
        count += 1
    
seoul = ["Jane", "Kim"]
solution(seoul)