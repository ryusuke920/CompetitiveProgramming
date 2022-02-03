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

a, b = map(int,input().split())

from collections import defaultdict
d = defaultdict(int)

for i in range(b + 1, a + 1):
    num = factorization(i)
    for j, k in num:
        d[j] += k

ans = 1
mod = 10 ** 9 + 7
for i in d.values():
    ans *= (i + 1)
    ans %= mod

print(ans)