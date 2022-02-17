def solution(progresses, speeds):
    answer = []

    term = []
    for i in range(len(progresses)):
        days = 0
        while(progresses[i] < 100):
            days += 1
            progresses[i] += speeds[i]

        term.append(days)
    
    count = 1
    max_term = term[0]
    for i in range(1, len(term)+1):
        if i == len(term):
            answer.append(count)
            break

        if term[i] < max_term or term[i] == max_term:
            count += 1
        elif term[i] > max_term:
               answer.append(count)
               max_term = term[i]
               count = 1
        
    return answer

