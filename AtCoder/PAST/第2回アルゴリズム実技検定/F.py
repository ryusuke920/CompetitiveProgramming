from heapq import heapify, heappush, heappop
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n):
    a, b = map(int,input().split())
    g[a - 1].append(b)

q = []
heapify(q)
ans = 0
for i in range(n):
    for j in g[i]:
        heappush(q, -j)
    ans += -heappop(q)
    print(ans)