def solution(arr):
    answer = []
    
    min_num = 1000000
    
    idx = 0
    for i in range(len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
            idx = i
    
    arr.pop(idx)
    if len(arr) == 0:
        answer = [-1]
    else:
        answer = arr
        
    return answer
