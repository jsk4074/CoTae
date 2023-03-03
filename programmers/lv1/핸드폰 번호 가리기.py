def solution(phone_number):
    return len(phone_number[:-4]) * '*' + phone_number[-4:]

phone_number, _ = "027778888", "*****8888"
phone_number, _ = "01033334444", "*******4444"
solution(phone_number)