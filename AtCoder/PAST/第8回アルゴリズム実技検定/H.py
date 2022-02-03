import sys
sys.setrecursionlimit(10 ** 6)

n, x = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append((c, b))
    g[b].append((c, a))

flag = False
def dfs(now: int, pre: int, dist: int):
    global flag
    if dist == x:
        flag = True
    for d, net in g[now]:
        if net == pre: continue
        dfs(net, now, dist + d)

for i in range(n):
    dfs(i, i - 1, 0)

if flag:
    print("Yes")
else:
    print("No")