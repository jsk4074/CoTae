# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    s = s[::-1]
    answer = []
    count = 0

    for i in s:
        location = s.find(i, count + 1) - count
        if location < 0:
            answer.append(-1)
        else: 
            answer.append(location)
        count += 1

    return answer[::-1]

# [-1, -1, -1, 2, 2, 2]
s = "banana"	
solution(s)