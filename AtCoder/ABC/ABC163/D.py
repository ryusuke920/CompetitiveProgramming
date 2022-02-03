n, k = map(int,input().split())
mod = 10 ** 9 + 7
ans = k * n - (k - 1) * k + 1
cnt = ans
for i in range(k + 1, n + 2):
    d = n - 2 * (i - 1)
    cnt += d
    ans += cnt
    ans %= mod
print(ans)