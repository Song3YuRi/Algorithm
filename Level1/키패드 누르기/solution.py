def solution(numbers, hand):
    answer = ''

    lastL = 10
    lastR = 12

    for n in numbers:
        if n == 0:
            n = 11

        idx = n % 3
        
        if idx == 1:
            answer += "L"
            lastL = n
        elif idx == 0:
            answer += "R"
            lastR = n
        elif idx == 2:
            cordinate_L = {"x" : 0, "y": 0}
            cordinate_R = {"x" : 0, "y": 0}
            cordiante_N = {"x": 0,  "y": 0}

            x = lastL // 3 - 1 if lastL % 3 == 0 else lastL // 3
            y = 3 if lastL % 3 == 0 else lastL % 3
            cordinate_L["x"] = x
            cordinate_L["y"] = y

            x = lastR // 3 - 1 if lastR % 3 == 0 else lastR // 3
            y = 3 if lastR % 3 == 0 else lastR % 3
            cordinate_R["x"] = x
            cordinate_R["y"] = y

            x = n // 3 - 1 if n % 3 == 0 else n // 3
            y = 3 if n % 3 == 0 else n % 3
            cordiante_N["x"] = x
            cordiante_N["y"] = y

            distanceL = (cordinate_L["x"] - cordiante_N["x"])**2 + (cordinate_L["y"] - cordiante_N["y"])**2
            distanceR = (cordinate_R["x"] - cordiante_N["x"])**2 + (cordinate_R["y"] - cordiante_N["y"])**2

            if float(distanceL) == float(distanceR):
                if hand == "right":
                    answer += "R"
                    lastR = n
                else:
                    answer += "L"
                    lastL = n
            elif float(distanceL) > float(distanceR):
                answer += "R"
                lastR = n
            else:
                answer += "L"
                lastL = n


    return answer
