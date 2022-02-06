n = int(input())

d = len(str(n))
mod = 998244353

ans = 0
for i in range(1, d):
    cnt = 10 ** i - 10 ** (i - 1)
    ans += cnt * (cnt + 1) // 2
    ans %= mod

t = 10 ** (d - 1)
cnt = n - t + 1

ans +=cnt * (cnt + 1) // 2
ans %= mod
print(ans)