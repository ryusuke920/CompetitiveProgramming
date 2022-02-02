from heapq import heapify, heappop, heappush

n, m = map(int,input().split())
g = [[] for _ in range(n)]
num = 0
for _ in range(m):
    u, v, l = map(int,input().split())
    u -= 1
    v -= 1
    g[u].append((l, v))
    g[v].append((l, u))
    num += l

q = []
q.append((0, 0))
heapify(q)
connection = 0
ans = 0
check = [False] * n
while q:
    cost, v = heappop(q)
    if check[v]: continue
    check[v] = True
    connection += 1
    ans += cost
    for i in g[v]:
        if check[i[1]]: continue
        heappush(q, i)
    
    if connection == n:
        break

print(num - ans)