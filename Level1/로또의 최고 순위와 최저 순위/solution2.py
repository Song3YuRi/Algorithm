def solution(lottos, win_nums):
    answer = []
    
    zero_count = 0
    answer_nums = 0

    for i in lottos:
        if i == 0:
            zero_count += 1
        
        for j in win_nums:
            if i == j:
                answer_nums += 1
    
    high_record = zero_count + answer_nums

    if high_record <= 1:
        answer.append(6)
    else:
        answer.append(7 - high_record)
    
    if answer_nums <= 1:
        answer.append(6)
    else:
        answer.append(7 - answer_nums)

    return answer
