import sys
sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
x = list(map(int, input().split()))
g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

ans = [[] for _ in range(n)]

def dfs(now: int, pre: int) -> None:
    ans[now].append(x[now])
    for nxt in g[now]:
        if nxt == pre: continue
        dfs(nxt, now)
        ans[now] += ans[nxt]
    ans[now].sort(reverse=True)
    ans[now] = ans[now][:20]


dfs(0, -1)

for _ in range(q):
    v, k = map(int, input().split())
    v -= 1
    k -= 1
    print(ans[v][k])