import math

def solution(n):
    answer = 0
    
    sqrt = int(math.sqrt(n))
    
    if(n == 1):
        answer = 1
    else:
        for i in range(1, sqrt+1):
            if n % i == 0:
                answer += i
                quotient = n // i
                if i != quotient:
                    answer += quotient
    
    return answer
