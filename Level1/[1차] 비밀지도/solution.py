def solution(n, arr1, arr2):
    answer = []

    binary1 = []
    binary2 = []

    total_binary = []

    for i in arr1:
        num = i
        binary_string = ''
        while(num >= 1):
            binary_string += str(num % 2)
            num = num // 2
        
        if len(binary_string) != n:
            lenght = n - len(binary_string)
            binary_string = binary_string + '0' * lenght
        
        tmp = ''
        for b in range(len(binary_string) - 1, -1, -1):
            tmp += binary_string[b]
        
        binary1.append(tmp)

    for i in arr2:
        num = i
        binary_string = ''
        while(num >= 1):
            binary_string += str(num % 2)
            num = num // 2
        
        if len(binary_string) != n:
            lenght = n - len(binary_string)
            binary_string = binary_string + '0' * lenght
        
        tmp = ''
        for b in range(len(binary_string) - 1, -1, -1):
            tmp += binary_string[b]
        
        binary2.append(tmp)
    
    for i in range(len(binary1)):
        secretmap = ''
        for b in range(len(binary1[i])):
            tmp = str(int(binary1[i][b]) or int(binary2[i][b]))
            if tmp == '1':
                secretmap += '#'
            elif tmp == '0':
                secretmap += ' '

        total_binary.append(secretmap)
    
    answer = total_binary
    print("total_binary : ", total_binary)
    return answer
