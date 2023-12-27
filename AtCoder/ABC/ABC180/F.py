import sys
input = sys.stdin.readline

def calc_cost(a: int, b: int, c: int, p: int, q: int, r: int) -> int:
    return abs(p - a) + abs(q - b) + max(0, r - c)

n = int(input())
x, y, z = [0] * n, [0] * n, [0] * n
for i in range(n):
    x[i], y[i], z[i] = map(int, input().split())

# dp[i][j] := 集合2^i に対して最後に訪れたまちが j の時の最小コスト
INF = 10**18
dp = [[INF] * (n + 1) for _ in range(2**n)]
dp[0][0] = 0

for s in range(2**n):
    # u -> v に行く場合
    for u in range(n):
        for v in range(n):
            # 既に訪問先が行ってたらダメ
            if (s >> v) & 1:
                continue
            # 既に訪問した集合 S の中に u が入っていないといけないもしくは初回のみはどこでも行けるので s == 0である必要がある
            if (s >> u) & 1 or s == 0:
                dp[s | 1 << v][v] = min(dp[s | 1 << v][v], dp[s][u] + calc_cost(x[u], y[u], z[u], x[v], y[v], z[v]))

#print(*dp, sep="\n")
print(dp[2**n - 1][0])