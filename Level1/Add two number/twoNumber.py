def solution(numbers):
    answer = []
    
    result = set()
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            result.add(numbers[i] + numbers[j])
    
    for i in result:
        answer.append(i)
    
    answer.sort()
    return answer