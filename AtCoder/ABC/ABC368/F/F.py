def g(limit):
    grundy = [0] * (limit + 1)
    
    for i in range(2, limit + 1):
        s = set()
        
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                if j < i:
                    s.add(grundy[j])
                if i // j < i:
                    s.add(grundy[i // j])
        
        g = 0
        while g in s:
            g += 1
        
        grundy[i] = g
    
    return grundy

def f(N, A):
    limit = max(A)
    grundy = g(limit)
    
    xor_sum = 0
    for a in A:
        xor_sum ^= grundy[a]
    
    if xor_sum != 0:
        return "Anna"
    else:
        return "Bruno"

N = int(input())
A = list(map(int, input().split()))

print(f(N, A))
