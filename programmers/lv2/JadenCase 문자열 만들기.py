def solution(s):
    word_list = []
    for i in s.split(' '):
        if i != '':
            word_list.append(i[0].upper() + i[1:].lower())
        else: 
            word_list.append('')
    return ' '.join(word_list)
    # return ' '.join([i[0].upper() + i[1:].lower() for i in s.split(' ') if i != ''])

s = "a aa "
# "3people Unfollowed Me"
print(solution(s) == "A Aa ")
solution(s)