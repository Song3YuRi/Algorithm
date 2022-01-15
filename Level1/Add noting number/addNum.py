def solution(numbers):
    answer = 0
    total_number = [0,1,2,3,4,5,6,7,8,9]

    for i in total_number:
        if i not in numbers:
            answer += i
    
    print("answer : ", answer)
    return answer

solution([5,8,4,0,6,7,9])