def solution(n, lost, reserve):
    answer = 0

    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)

    get_clothes = set()

    print("new_lost : ", new_lost)
    print("new_reserve : ", new_reserve)
    
    for i in new_lost:
        pre_num = {i - 1}
        next_num = {i + 1}
        print("l : ", i)

        if new_reserve.intersection(pre_num) == pre_num:
            new_reserve = new_reserve - pre_num
            get_clothes.add(i)
        elif new_reserve.intersection(next_num) == next_num:
            new_reserve = new_reserve - next_num
            get_clothes.add(i)
    
    real_lost = new_lost - get_clothes
    print("get_clothes : ", get_clothes)
    print("real_lost : ", real_lost)
    answer = n - len(real_lost)

    print("answer : ", answer)
    return answer
