import sys
input = sys.stdin.readline
sys.setrecursionlimit(500_000)

def dfs(now: int, prev: int):
    global num
    cnt = 0
    for nxt, cost in g[now]:
        if nxt == prev:
            continue
        cnt += 1
    
    if cnt == 1:
        for nxt, cost in g[now]:
            if nxt == prev:
                continue
            num += cost
            dfs(nxt, now)

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    g[A].append((B, C))
    g[B].append((A, C))


sum_cost = 0
for i in range(N):
    for _, cost in g[i]:
        sum_cost += cost

INF = 10**18

l = []
for i in range(N):
    if len(g[i]) == 1:
        num = 0
        dfs(i, -1)
        l.append(num)

ans = INF
if len(l) == 2:
    ans = min(ans, sum_cost - l[0])
else:
    l.sort()
    ans = min(ans, sum_cost - (l[0] + l[1]))

print(ans)