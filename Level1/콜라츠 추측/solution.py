def collatz(count, num):
    if num == 1:
        return count, num
    
    if num % 2 == 0:
        num = num // 2
    else:
        num = (num * 3 ) + 1
    
    count += 1
    return count, num

def solution(num):
    answer = 0
    
    count = 0
    while(count < 500):
        [count, num] = collatz(count, num)
        if num == 1:
            answer = count
            break
    
    if count >= 500:
        answer = -1
        
    return answer
