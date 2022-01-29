def solution(n):
    answer = ''
    pattern = ['수', '박']
    
    for i in range(n):
        if i % 2 != 1:
            answer += pattern[0]
        else:
            answer += pattern[1]
            
    return answer
