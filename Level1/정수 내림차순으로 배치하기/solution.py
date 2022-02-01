def solution(n):
    answer = 0
    
    num_list = []
    n = str(n)
    
    for i in n:
        num_list.append(i)
    
    num_list.sort(reverse=True)
    
    answer = ''.join(num_list)
    
    answer = int(answer)
    return answer
