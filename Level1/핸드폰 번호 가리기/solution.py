def solution(phone_number):
    idx = len(phone_number) - 4
    answer = '*' * idx
    
    for i in range(idx, len(phone_number)):
        answer += phone_number[i]
        
    return answer
