n, K = map(int,input().split())
c, k = [0] * K, [0] * K
for i in range(K):
    c[i], k[i] = map(str, input().split())
    k[i] = int(k[i])

num = [K] * n
INF = 10 ** 6
for i in range(K):
    num[k[i] - 1] = INF
    if c[i] == "L":
        for j in range(k[i] - 1):
            if num[j] != INF:
                num[j] -= 1
    elif c[i] == "R":
        for j in range(n - k[i]):
            if num[-1-j] != INF:
                num[-1 - j] -= 1

mod = 998244353
ans = 1
for i in range(n):
    if num[i] == INF: continue
    ans *= num[i]
    ans %= mod

print(ans % mod)