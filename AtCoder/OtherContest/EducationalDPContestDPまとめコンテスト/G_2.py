import sys
sys.setrecursionlimit(10 ** 8)
n, m = map(int,input().split())
g = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int,input().split())
    g[x - 1].append(y - 1)

done = [False] * n
memo = [0] * n

def dp(v: int) -> int:
    if done[v]: return memo[v]
    num = 0
    for i in g[v]:
        num = max(num, dp(i) + 1)
    memo[v] = num
    done[v] = True
    return memo[v]

ans = 0
for i in range(n):
    ans = max(ans, dp(i))

print(ans)