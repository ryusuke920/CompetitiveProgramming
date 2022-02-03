N, K = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
mod = 10 ** 9 + 7
ans = 0

nCk = 1
# max(A)を求める
for i in range(max(0, N - K + 1)):
    if i == 0:
        nCk = 1
    else:
        nCk *= (K + i - 1)
        nCk *= pow(i, -1, mod)
    nCk %= mod

    ans += a[K + i - 1] * nCk
    ans %= mod

nCk = 1
# min(A)を求める
for i in range(max(0, N - K + 1)):
    if i == 0:
        nCk = 1
    else:
        nCk *= (K + i - 1)
        nCk *= pow(i, -1, mod)
    nCk %= mod

    ans -= a[N - K - i] * nCk
    ans %= mod

print(ans)