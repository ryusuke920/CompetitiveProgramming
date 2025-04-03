n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    s, t, d, time = map(int, input().split())
    g[s - 1].append((t - 1, d, time))
    g[t - 1].append((s - 1, d, time))

INF = 10 ** 18
dp = [[[INF, 0]] * n for _ in range(2 ** n)]
dp[0][0] = [0, 1]
# dp[i][j] := 今 i にいて、 頂点 j を訪れたまでの[最短経路, 通り数]

for S in range(2 ** n):
    for u in range(n):
        if (S >> u) & 1 == 0 and S != 0: continue
        for v, d, time in g[u]:
            if (S >> v) & 1 == 1: continue
            if dp[S][u][0] + d > time: continue
            if dp[S | (1 << v)][v][0] > dp[S][u][0] + d:
                dp[S | (1 << v)][v] = [dp[S][u][0] + d, dp[S][u][1]]
            elif dp[S | (1 << v)][v][0] == dp[S][u][0] + d:
                dp[S | (1 << v)][v][1] += dp[S][u][1]

print(*dp[-1][0]) if dp[-1][0][0] != INF else print('IMPOSSIBLE')