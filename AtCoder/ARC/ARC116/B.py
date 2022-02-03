n = int(input())
a = list(map(int,input().split()))
mod = 998244353
a.sort()
num = 0
ans = 0
for i in range(n - 1):
    num *= 2
    num += a[-1 - i]
    num %= mod
    ans += a[-2 - i] * num
    ans %= mod

# 各要素の２乗を計算
s = 0
for i in range(n):
    s += a[i] ** 2
    s %= mod

ans += s
print(ans % mod)