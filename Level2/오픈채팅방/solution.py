def solution(record):
    answer = []
    
    user = {}
    action = []
    
    for i in record:
        words = i.split(' ')
        if len(words) == 3:
            user[words[1]] = words[2]
            
    for i in record:
        words = i.split(' ')
        user_id = words[1]
        if words[0] == "Enter":
            answer.append(user[user_id] + "님이 " + "들어왔습니다.")
        elif words[0] == "Leave":
            answer.append(user[user_id] + "님이 " + "나갔습니다.")
            
    return answer
