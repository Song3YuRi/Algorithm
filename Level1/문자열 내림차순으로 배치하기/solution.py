def solution(s):
    answer = ''
    
    Up = ''
    Lower = ''
    
    for i in s:
        if i.isupper():
            Up += i
        else:
            Lower += i

    s1 = ''.join(sorted(Lower, reverse=True))
    s2 = ''.join(sorted(Up, reverse=True))

    answer = s1 + s2
    
    return answer
