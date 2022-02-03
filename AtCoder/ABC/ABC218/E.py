from heapq import heappop, heappush, heapify

n, m = map(int,input().split())
g = [[] for _ in range(n)]

ans = 0
for _ in range(m):
    a, b, c = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append((c, b))
    g[b].append((c, a))
    ans += max(0, c)

q = []
q.append((0, 0))
heapify(q)
check = [0] * n
connection = 0

# 正の辺だけ全て取り除く（報酬の最大値） -> 最小全域木をする（報酬が減っていく -> 減る量の最小値を求める）
while q:
    cost, v = heappop(q)
    if check[v]: continue

    check[v] = 1
    connection += 1
    ans -= max(0, cost)

    for i in g[v]:
        if check[i[1]]: continue
        heappush(q, i)
    
    if connection == n: break

print(ans)