def solution(n):
    answer = 0

    triad = ''
    while n >= 1:
        tmp = n % 3
        triad += str(tmp)
        n = n // 3
    
    idx = len(triad) - 1
    for i in range(len(triad)):
        num = 3**i
        num = num * int(triad[idx])

        answer += num
        idx -= 1
    return answer
