def primes_list(n):
    if n == 0:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]: continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

from collections import defaultdict
d = defaultdict(int)

n, k = map(int,input().split())
mod = 998244353

# 分子
a = [n - i for i in range(k)]
num = primes_list(int(n ** 0.5) + 1)

for p in num:
    for i in reversed(range(n - k + 1 + p - (n - k + 1) % p if (n - k + 1) % p != 0 else n - k + 1, n + 1, p)):
        while a[n - i] % p == 0:
            d[p] += 1
            a[n - i] //= p

for i in range(len(a)):
    if a[i] != 1:
       d[a[i]] += 1

# 分母
a = [i for i in range(k + 1)]
num = primes_list(k) # 素数の全列挙

for p in num:
    for i in range(p, k + 1, p):
        while a[i] % p == 0:
            d[p] -= 1
            a[i] //= p

ans = 1
for i, j in d.items():
    if j >= 1:
        ans *= (j + 1)
        ans %= mod

print(ans)