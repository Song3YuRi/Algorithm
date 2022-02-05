def solution(x):
    answer = True
    
    str_x = str(x)
    puls_num = 0
    
    for i in str_x:
        puls_num += int(i)
    
    if x % puls_num != 0:
        answer = False
        
    return answer
