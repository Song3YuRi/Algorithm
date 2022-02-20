import itertools

def solution(orders, course):
    answer = []
    number_order = dict()
    
    max_keys = dict()
    max_values = dict()

    for c in course:
        max_keys[c] = []
        max_values[c] = 2

        for o in orders:
            if len(o) >= c:
                result  = list(itertools.combinations(sorted(o), c))
                
                for k in result:
                    number_order[k] = number_order.get(k, 0) + 1

    number_order = sorted(number_order.items(), key = lambda x : x[1], reverse=True)

    for i in number_order:
        c = len(i[0])
        if max_values[c] <= i[1]:
            max_values[c] = i[1]
            max_keys[c].append(i[0])

    for i in max_keys:
        for j in max_keys[i]:
            tmp = ''
            for k in j:
                tmp += k

            answer.append(tmp)

    answer.sort()
    
    return answer
