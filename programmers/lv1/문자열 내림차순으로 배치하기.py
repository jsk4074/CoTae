def solution(s):
    return ''.join(reversed(sorted(s)))

s, _ = "Zbcdefg", "gfedcbZ"
solution(s)