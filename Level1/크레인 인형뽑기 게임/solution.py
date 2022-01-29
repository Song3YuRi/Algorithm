def solution(board, moves):
    answer = 0
    basket = []

    for i in moves:
        for j in range(len(board)):
            num = board[j][i-1]
            if num == 0:
                continue
            else:
                basket.append(num)
                board[j][i-1] = 0
                
                if len(basket) > 1 :
                    if basket[-1] == basket[-2]:
                        answer += 2
                        basket.pop()
                        basket.pop()
                break

    print("answer : ", answer)
    return answer
