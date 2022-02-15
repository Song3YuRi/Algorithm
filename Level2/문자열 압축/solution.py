def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        strings = []
        s_tmp = s

        for j in range(0, len(s), i):
            tmp = s[j:j+i]
            strings.append(tmp)

        count = 1
        for j in range(len(strings) - 1):
            prev = strings[j]
            next = strings[j+1]

            if prev == next:
                count += 1
                if j+1 == len(strings) - 1:
                    s_tmp = s_tmp.replace(prev, '', count-1)
                    s_tmp = s_tmp.replace(prev, str(count)+prev, 1)
                    count = 1
            elif prev != next and count != 1:
                s_tmp = s_tmp.replace(prev, '', count-1)
                s_tmp = s_tmp.replace(prev, str(count)+prev, 1)
                count = 1
        

        if len(s_tmp) < answer:
            print("i : ", i)
            answer = len(s_tmp)   
            
    return answer
