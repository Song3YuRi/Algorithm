def solution(a, b):
    answer = ''
    
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    days = 0
    for i in range(a - 1):
        days += month[i]
    
    days += b

    answer = week[days % 7]
    return answer
