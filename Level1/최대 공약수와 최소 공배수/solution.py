def get_GCD(a, b):
    if a % b == 0:
        return b
    else:
        return get_GCD(b, a%b)

def solution(n, m):
    answer = []
    
    gcd = 0
    while(gcd == 0):
        if n > m:
            gcd = get_GCD(n, m)
        else:
            gcd = get_GCD(m, n)
    
    lcm = (n*m) // gcd
    answer.append(gcd)
    answer.append(lcm)
    return answer
