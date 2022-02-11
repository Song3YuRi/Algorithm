def solution(s):
    answer = 0

    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(len(numbers)):
        answer.replace(alpha[i], numbers[i])
    
    answer = int(answer)
    return answer
