import re

def solution(s):
    answer = 0
    s = re.sub(r"zero", "0", s)
    s = re.sub(r"one", "1", s)
    s = re.sub(r"two", "2", s)
    s = re.sub(r"three", "3", s)
    s = re.sub(r"four", "4", s)
    s = re.sub(r"five", "5", s)
    s = re.sub(r"six", "6", s)
    s = re.sub(r"seven", "7", s)
    s = re.sub(r"eight", "8", s)
    s = re.sub(r"nine", "9", s)        
    print("S : ", s)
    answer = int(s)
    return answer
  
