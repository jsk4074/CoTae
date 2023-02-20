def solution(s):
    return ' '.join([str(min([int(i) for i in list(s.split())])),str(max([int(i) for i in list(s.split())]))])

s = "1 2 3 4"	
s = "-1 -2 -3 -4"	
# "1 4"
solution(s)