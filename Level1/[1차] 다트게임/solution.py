import re

def solution(dartResult):
    answer = 0

    point = []
    m = re.match('([0-9]+\D\D?)([0-9]+\D\D?)([0-9]+\D\D?)', dartResult)
    point_string = []
    for i in range(1, 4):
        point_string.append(m.group(i))
    
    print("point string : ", point_string)
    for i in point_string:
        get_point = 0

        m = re.match('([0-9]+)', i)
        number = m.group(1)

        string = i.replace(number, '')
        print("number : ", number)
        print("string : ", string)

        get_point = int(number)

        for s in string:
            if s == 'S':
                get_point = get_point ** 1
            elif s == 'D':
                get_point = get_point ** 2
            elif s == 'T':
                get_point = get_point ** 3
            elif s == '*':
                if len(point) == 0:
                    get_point = get_point * 2
                else:
                    point[-1] = point[-1] * 2
                    get_point = get_point * 2
            elif s == '#':
                get_point = get_point * -1
        
        point.append(get_point)
    
    print("point : ", point)
    for p in point:
        answer += p
    
    print("answer : ", answer)

    return answer

solution('10D4S10D')
