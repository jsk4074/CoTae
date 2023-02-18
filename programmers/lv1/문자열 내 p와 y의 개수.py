def solution(s):
    if list(s.lower()).count('p') == list(s.lower()).count('y'):
        return True
    else:
        return False

s = "pPoooyY"	
solution(s)