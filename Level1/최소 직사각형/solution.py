def solution(sizes):
    answer = 0

    max_heigth = 0
    max_width = 0

    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            tmp = sizes[i][1]
            sizes[i][1] = sizes[i][0]
            sizes[i][0] = tmp

    for i in range(len(sizes)):
        if sizes[i][1] > max_heigth:
            max_heigth = sizes[i][1]
        
        if sizes[i][0] > max_width:
            max_width = sizes[i][0]

    answer = max_width * max_heigth

    print("answer : ", answer)
    print("sizes : ", sizes)

    return answer

