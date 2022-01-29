import math


def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        
        primeNumber = [1]

        if i != 1:
            sqrt = int(math.sqrt(i))

            for k in range(2, sqrt+1):
                if i % k == 0:
                    primeNumber.append(k)
                    if i // k != k:
                        primeNumber.append(i // k)
            
            primeNumber.append(i)

        if len(primeNumber) % 2 == 0:
            answer += i
        else:
            answer -= i
        
        print("number : ", i)
        print("primeNumber : ", primeNumber)
        print("answer : ", answer)
        
    return answer
