import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub(r"[~!@#$%^&*()=+[{\]}:?,<>/]", "", new_id)
    new_id = re.sub(r"[.]{2,}", ".", new_id)
    new_id = re.sub(r"^[.]", "", new_id)
    new_id = re.sub(r"[.]$", "", new_id)
    if new_id == "":
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = re.sub(r"[.]$", "", new_id)
    if len(new_id) <= 2:
        while len(new_id) != 3:
            last_word = new_id[-1]
            print("last_word : ", last_word)
            new_id = new_id + last_word
    
    print("new_id : ", new_id)
    print(len(new_id))     
    answer = new_id
    return answer
