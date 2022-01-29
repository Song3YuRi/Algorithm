def solution(s, n):
    answer = ''
    for i in s:
        if i != ' ':
            i = ord(i)
            if i >= 65 and i <= 90:    
                i += n
                if i > 90:
                    gap = i - 90
                    i = 64 + gap
                    answer += chr(i)
                else:
                    answer += chr(i)
            elif i >= 97 and i <= 122:
                i += n
                if i > 122:
                    gap = i - 122
                    i = 96 + gap
                    answer += chr(i)
                else:
                    answer += chr(i)
        else:
            answer += ' '
    
    return answer
