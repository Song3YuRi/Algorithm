def solution(places):
    answer = []

    for i in places:
        # p들의 좌표 구하기
        p_coordinate = []
        for j  in range(len(i)):
            for k in range(len(i[j])):
                if i[j][k] == 'P':
                    p_coordinate.append((j, k))

        # print("P들의 좌표 : ", p_coordinate)
        
        check_p = []
        # 맨해튼 거리 체크 
        for p1 in range(len(p_coordinate) - 1):
            for p2 in range(p1 + 1, len(p_coordinate)):
                space = abs(p_coordinate[p1][0] - p_coordinate[p2][0]) + abs(p_coordinate[p1][1] - p_coordinate[p2][1])
                if space < 3:
                    check_p.append([p_coordinate[p1], p_coordinate[p2]])

        # 맨해튼 거리가 2이하인것들 사이에 빈 책상 체크
        # print("check_p : ", check_p)
        if len(check_p) == 0:
            answer.append(1)
        else:
            add_answer = 1
            for p1 in check_p:
                # print('p1 : ', p1)
                x1 = p1[0][0]
                x2 = p1[1][0]
                y1 = p1[0][1]
                y2 = p1[1][1]

                if x1 == x2:
                    # print("palces : ", i[x1 - 1][abs(y1-y2) - 1])
                    if i[x1][min(y1, y2) + 1] != 'X':
                        add_answer = 0
                        break
                
                if y1 == y2:
                    # print("palces : ", i[abs(x1-x2)][y1])
                    if i[min(x1, x2) + 1][y1] != 'X':
                        add_answer = 0
                        break
                    
                if x1 != x2 and y1 != y2:
                    # print("palces : ", i[x1][y2])
                    # print("palces : ", i[x2][y1])
                    if i[x1][y2] != 'X':
                        add_answer = 0
                        break
                    elif i[x2][y1] != 'X':
                        add_answer = 0
                        break

            answer.append(add_answer)

    
    return answer
