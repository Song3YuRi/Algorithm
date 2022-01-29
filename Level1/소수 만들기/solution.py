import math

def solution(nums):
    answer = 0

    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                number = nums[i] + nums[j] + nums[k]

                # print("number : ", number)
                if number % 2 != 0:
                    sqrt = int(math.sqrt(number))

                    print("sqrt : ", sqrt)
                    check = 0
                    if sqrt >= 3:
                        for n in range(2, sqrt+1):
                            print()
                            if number % n == 0:
                                check += 1
                    
                    if check == 0:
                        print("number : ", number)
                        answer += 1
    
    print("answer : ", answer)
    return answer

solution([1,2,7,6,4])
