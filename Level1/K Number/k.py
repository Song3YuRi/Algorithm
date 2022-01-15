def solution(array, commands):
    answer = []
    
    for c in commands:
        print(c)
        tmp_array = []

        for a in range(c[0] - 1, c[1]):
            # print("a : ", array[a])
            tmp_array.append(array[a])
        
        tmp_array.sort()
        answer.append(tmp_array[c[2] - 1])
    
    print("answer : ", answer)
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])