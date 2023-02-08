def solution(babbling):
    babble_list = ["aya", "ye", "woo", "ma"]
    answer = []

    for j in babbling:
        if j == "": continue
        for i in babble_list:
            j = j.replace(i, "*")

        answer.append(j)

    return [set(tmp) for tmp in answer].count({"*"})