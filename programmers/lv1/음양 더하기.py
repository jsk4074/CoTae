def solution(absolutes, signs):
    return sum([absolutes[i] for i in range(len(signs)) if signs[i]]) - sum([absolutes[i] for i in range(len(signs)) if signs[i] == False])

absolutes, signs = [4,7,12], [True, False, True] # 9

solution(absolutes, signs)