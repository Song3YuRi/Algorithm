def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        idx = len(s) // 2
        answer = s[idx - 1] + s[idx]
    else:
        idx = (len(s) - 1) // 2
        answer = s[idx]
    
    return answer