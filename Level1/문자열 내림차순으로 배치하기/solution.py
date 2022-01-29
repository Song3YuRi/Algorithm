def solution(s):
    answer = ''
    
    Up = ''
    Lower = ''
    
    for i in s:
        if i.isupper():
            Up += i
        else:
            Lower += i
    
    for i in range(len(Lower) - 1, 0, -1):
        for j in range(0, i):
            if Lower[j] < Lower[j+1]:
                tmp = Lower[j]
                Lower[j] = Lower[j+1]
                Lower[j+1] = tmp
    
    for i in range(len(Up) - 1, 0, -1):
        for j in range(0, i):
            if Up[j] < Up[j+1]:
                tmp = Up[j]
                Up[j] = Up[j+1]
                Up[j+1] = tmp
    
    answer = Lower + Up
    return answer
