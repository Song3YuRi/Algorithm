def solution(N, stages):
    answer = []

    failure = {}

    total = len(stages)
    for i in range(1, N+1):
        if total != 0:
            count = stages.count(i)
            failure[i] = count / total
            total -= count
        else:
            failure[i] = 0
    
    return sorted(failure, key=lambda x : failure[x], reverse=True)
