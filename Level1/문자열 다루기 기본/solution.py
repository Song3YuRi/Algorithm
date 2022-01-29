import re

def solution(s):
    answer = True
    
    if(len(s) == 6 or len(s) == 4):
        p = re.search('[a-zA-Z]', s)
        if p != None:
            answer = False
    else:
        answer = False
    
    return answer
