import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
mod = 998244353
g = [[] for _ in range(N)]
for _ in range(M):
    u, v, t = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, t))
    g[v].append((u, t))

inv = [pow(len(g[i]), mod - 2, mod) for i in range(N)]
dp = [[0] * (T + 1) for _ in range(N)]
dp[0][0] = 1
for t in range(T):
    for u in range(N - 1):
        for nxt, cost in g[u]:
            if t + cost > T:
                continue
            dp[nxt][t + cost] += dp[u][t] * inv[u]
            dp[nxt][t + cost] %= mod

ans = 0
for i in range(T + 1):
    ans += dp[N - 1][i]
    ans %= mod
print(ans)