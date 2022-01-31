def solution(s):
    answer = ''
    s_list = s.split(' ')
    empty = s.count(' ')
    
    for s in range(len(s_list)):
        tmp = ''
        for i in range(len(s_list[s])):
            if i % 2 == 0:
                tmp += s_list[s][i].upper()
            else:
                tmp += s_list[s][i].lower()

        answer += tmp
        if empty != 0:
            answer += ' '
            empty -= 1
    
    return answer
