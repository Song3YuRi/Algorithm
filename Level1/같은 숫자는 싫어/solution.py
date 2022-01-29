def solution(arr):
    answer = []
    
    idx = 0
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        
        if answer[idx] != i:
            answer.append(i)
            idx += 1
    return answer
