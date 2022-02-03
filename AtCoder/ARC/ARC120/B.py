h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]
# 斜めに見ていく
check = [[] for _ in range(h + w - 1)]

for i in range(h):
    for j in range(w):
        check[i+j].append(s[i][j])

ans = 1
mod = 998244353

for i in range(h + w - 1):
    if len(check[i]) == check[i].count("."):
        ans *= 2
        ans %= mod
    elif "R" in check[i] and "B" in check[i]:
        ans = 0

print(ans % mod)