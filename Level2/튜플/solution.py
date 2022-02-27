import re

def solution(s):
    answer = []
    s = s[1:-1]

    result = re.findall(r'\{[0-9]+[,0-9]*\}', s)
    for i in range(len(result)-1):
        for j in range(i+1, len(result)):
            if len(result[i]) > len(result[j]):
                tmp = result[i]
                result[i] = result[j]
                result[j] = tmp
    

    for i in result:
        number = i[1:-1]
        numbers = number.split(",")
        for n in numbers:
            if int(n) not in answer:
                answer.append(int(n))
    
    return answer
