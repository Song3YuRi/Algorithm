# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EC%99%84%EC%A0%84-%ED%83%90%EC%83%89-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-Python

from itertools import permutations

def sosu(n):
    if n < 2:
        return False
    
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
        
    return True    

def solution(numbers):
    answer = 0
    p = []
    result = []
    
    for i in range(1, len(numbers)+1):
        p.extend(permutations(numbers, i))
        result = [int(''.join(i)) for i in p]
    
    for i in set(result):
        if sosu(i):
            answer+=1
            
    return answer
