def solution(lottos, win_nums):
    answer = []
    count = 0
    zero = 0
    for i in lottos:
        if i == 0:
            zero += 1
        for j in win_nums:
            if i == j:
                print("lottos : ", i)
                print("win_nums : ", j)
                count += 1
    if count < 2:
        answer.append(6)
    else:
        answer.append(7 - count)
    count += zero
    if 7 - count >= 7:
        answer.append(6)
    else:
        answer.append(7 - count)
    answer.sort()
    return answer


lottos = [45, 4, 35, 20, 3, 9]		
win_nums = [1, 2, 5, 6, 11, 12]	
print(solution(lottos, win_nums))