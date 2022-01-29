def solution(N, stages):
    answer = []

    stage_rate = {}
    sort_list = []
    sort_key = []

    for i in range(1, N+1):
        
        total_count = 0
        count = 0
        for s in stages:
            if i == s or i < s:
                total_count += 1
                if i == s:
                    count += 1

        failure_rate = count / total_count 
        stage_rate[i] = failure_rate
        sort_list.append(failure_rate)
        sort_key.append(failure_rate)

    sort = stage_rate.keys()

    sort_list.sort(reverse=True)
    
    for i in sort_list:
        for key, value in stage_rate.items():
            if value == i:
                answer.append(key)
                del stage_rate[key]
                break

    print("answer : ", answer)
    print("sort_list : ", sort_list)
    return answer
