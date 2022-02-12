def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    one_index = 0
    two_index = 0
    three_index = 0

    count = [0, 0, 0]

    for i in answers:
        if one[one_index] == i:
            count[0] += 1
        if two[two_index] == i:
            count[1] += 1
        if three[three_index] == i:
            count[2] += 1
        
        one_index += 1
        if one_index == len(one):
            one_index = 0
        
        two_index += 1
        if two_index == len(two):
            two_index = 0

        three_index += 1
        if three_index == len(three):
            three_index = 0

    max_person = max(count)
    for i in range(len(count)):
        if max_person == count[i]:
            answer.append(i + 1)

    return answer
