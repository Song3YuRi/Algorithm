def solution(nums):
    answer = 0

    length = len(nums) / 2

    result = set()

    for i in nums:
        if i not in result and len(result) < length:
            result.add(i)
        
    print("result : ", result)
    answer = len(result)
    return answer

solution([3,1,2,3])
