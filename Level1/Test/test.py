def solution(answers):
    answer = []
    
    student = [0,0,0]
    for i in range(3):
        
        person_answer = i+1
        
        count = 1
        for a in answers:            
            if i == 0:
                if a == person_answer:
                    student[i] += 1
                    person_answer += 1
                else:
                    person_answer += 1
                
                if person_answer == 6:
                    person_answer = 1
            elif i == 1:
                if count % 2 != 0:
                    if person_answer == 2:
                        person_answer = 1
                        
                    if a == person_answer:
                        student[i] += 1
                    
                    if person_answer == 1:
                        person_answer += 2
                    else:
                        person_answer += 1
                    
                    if person_answer > 5:
                        person_answer = 1
                    
                    count += 1
                else:
                    if a == 2:
                        student[i] += 1
                    count += 1
            elif i == 2:
                
                if person_answer == a:
                    student[i] += 1
                    if count == 1:
                        count += 1
                    elif count == 2:
                        count = 1
                        if person_answer == 3:
                            person_answer = 1
                        else:
                            person_answer += 1
                        
                        if person_answer > 5:
                            person_answer = 3
                else:
                    if count == 1:
                        count += 1
                    elif count == 2:
                        count = 1
                        if person_answer == 3:
                            person_answer = 1
                        else:
                            person_answer += 1
                        
                        if person_answer > 5:
                            person_answer = 3    
    
    answer.sort()
    return answer