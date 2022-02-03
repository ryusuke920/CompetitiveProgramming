from heapq import heappop, heappush
from collections import defaultdict
n, m = map(int,input().split())
d = defaultdict(list)
for _ in range(n):
    a, b = map(int,input().split())
    d[a].append(b)

ans = 0
q = []
for i in range(m):
    for j in d[i + 1]:
        heappush(q, -j)
    
    if q:
        ans += -1 * heappop(q)

print(ans)