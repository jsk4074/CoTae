# This is art
def solution(today, terms, privacies):
    return [i + 1 for i in range(len(privacies)) if {i.split(' ')[0] : int(i.split(' ')[1]) * 28 for i in terms}[[i.split(' ')[1] for i in privacies][i]] <= [[int(today.split('.')[i]) - int(j.split(' ')[0].split('.')[i]) for i in range(3)][0] * 336 + [int(today.split('.')[i]) - int(j.split(' ')[0].split('.')[i]) for i in range(3)][1] * 28 + [int(today.split('.')[i]) - int(j.split(' ')[0].split('.')[i]) for i in range(3)][2] for j in privacies][i]]

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = [
    "2021.05.02 A", # 353
    "2021.07.01 B", # Trash
    "2022.02.19 C", 
    "2022.02.20 C", # Trash
]
today = "2020.01.01"	
terms = ["Z 3", "D 5"]
privacies = [
    "2019.01.01 D", 
    "2019.11.15 Z", 
    "2019.08.02 D", 
    "2019.07.01 D", 
    "2018.12.28 Z"
]
solution(today, terms, privacies)