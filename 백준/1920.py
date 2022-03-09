from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

for i in M:
    target_num = i
    
    min_idx = 0
    max_idx = len(N) - 1
    answer = 0
    while(min_idx <= max_idx):
        mid = (max_idx - min_idx) // 2
        mid = min_idx + mid

        # print("min_idx : ", min_idx)
        # print('max_idx : ', max_idx)
        # print("mid : ", mid)
        # print("N[mid] : ", N[mid])
        # print("target_num : ", target_num)


        if N[mid] == target_num:
            answer = 1
            break
        
        if N[mid] < target_num:
            min_idx = mid + 1
        else:
            max_idx = mid - 1
    
    print(answer)
        
