import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
g = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

for i in range(n):
    g[i].sort()

ans = []

def dfs(now: int, prev: int):
    ans.append(now + 1)
    for i in g[now]:
        if i != prev:
            dfs(i, now)
            ans.append(now + 1) # いけるところまで行ったら戻ってくるイメージ

dfs(0, -1)
print(*ans)