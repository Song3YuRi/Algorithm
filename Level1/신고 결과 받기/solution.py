def solution(id_list, report, k):
    answer = []

    total = {}
    reported_count = {}
    result = {}

    for i in id_list:
        total[i] = set()
        reported_count[i] = 0
        result[i] = 0

    for i in report:
        person = i.split(' ')
        if set.intersection(total[person[0]], { person[1]} ) != { person[1] }:
            reported_count[person[1]] += 1
            total[person[0]].add(person[1])

    for i in reported_count:
        if reported_count[i] >= k:
            for j in total:
                if set.intersection(total[j], { i }) == { i }:
                    result[j] += 1

    for i in result:
        answer.append(result[i])
    
    return answer
