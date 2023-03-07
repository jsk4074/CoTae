def solution(s):
    s_len = len(s) 
    if s_len % 2 == 1:
        return s[int(s_len/2)]
    else:
        return s[int(len(s)/2)-1:int(len(s)/2)+1]

s = "abcd"
s = "abcde"	
solution(s)