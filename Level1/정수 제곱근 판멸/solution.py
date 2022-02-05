import math

def solution(n):
    answer = 0
    sqrt = math.sqrt(n)
    point_num = str(sqrt).split('.')[1]
    if point_num == '0':
        answer = (int(sqrt) + 1)**2
    else:
        answer = -1
    
    return answer
