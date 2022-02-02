n = int(input())
c = list(map(int, input().split()))

mod = 10 ** 9 + 7

fac = [1] * (n + 1)
for i in range(n):
    fac[i + 1] = fac[i] * (i + 1) 
    fac[i + 1] %= mod

# 前処理
num = 1
for i in range(9):
    if fac[c[i]] == 0: continue
    num *= pow(fac[c[i]], -1, mod)

ans = 0
for k in range(0, n):
    for i in range(9):
        cnt = c[i] * fac[n - 1]
        cnt *= num
        cnt *= (i + 1)
        cnt *= pow(10, k, mod)
        cnt %= mod
        ans += cnt
        ans %= mod

print(ans)