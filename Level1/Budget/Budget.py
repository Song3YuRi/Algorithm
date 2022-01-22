def solution(d, budget):
    answer = 0

    estimation = 0
    d.sort()

    for i in d:
        estimation += i
        if estimation > budget:
            break
        else:
            answer += 1
        
    
    return answer