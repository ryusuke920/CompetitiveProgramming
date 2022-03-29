from collections import defaultdict

def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

n = int(input())

d = defaultdict(int)
for i in  range(1, n + 1):
    num = factorization(i)
    for k, v in num:
        d[k] += v

ans = 0
# 4, 4, 2
check = [[4, 4, 2], [4, 2, 4], [2, 4, 4]]
for i_k, i_v in d.items(): 
    for j_k, j_v in d.items():
        for k_k, k_v in d.items():
            if not (i_k < j_k < k_k): continue
            for i, j, k in check:
                if i_v >= i and  j_v >= j and k_v >= k:
                    ans += 1

# [14, 4], [24, 2]
check = [[14, 4], [4, 14], [24, 2], [2, 24]]
for i_k, i_v in d.items(): 
    for j_k, j_v in d.items():
        if not (i_k < j_k): continue
        for i, j in check:
            if i_v >= i and  j_v >= j:
                ans += 1

# 74
for i_k, i_v in d.items():
    if i_v >= 74:
        ans += 1

print(ans)