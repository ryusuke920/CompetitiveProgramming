w, h = map(lambda x: int(x) - 1, input().split())

mod = 10 ** 5

nCk = [[0] * 300 for _ in range(300)]
nCk[0][0] = 1

for i in range(1, 300):
    nCk[i][0] = 1
    for j in range(i + 1):
        nCk[i][j] = nCk[i - 1][j - 1] + nCk[i - 1][j]
        nCk[i][j] %= mod

def com(n: int, k: int) -> int:
    if not (0 <= k <= n): return 0
    return nCk[n][k]

ans = 0
# 上・上
for k in range(1, max(h, w) + 1):
    ans += com(h - k, k) * com(w - k - 1, k - 1)
    ans %= mod

# 上・右
for k in range(1, max(h, w) + 1):
    ans += com(h - k, k - 1) * com(w - k, k - 1)
    ans %= mod

# 右・上
for k in range(1, max(h, w) + 1):
    ans += com(h - k, k - 1) * com(w - k, k - 1)
    ans %= mod

# 右・右
for k in range(1, max(h, w)):
    ans += com(h - k - 1, k - 1) * com(w - k, k)
    ans %= mod

print(ans)