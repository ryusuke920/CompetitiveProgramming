n, k = map(int, input().split())
p = list(map(int, input().split()))

from heapq import heapify, heappop, heappush
q = []
heapify(q)
for i in range(k):
    heappush(q, p[i])

a = heappop(q)
print(a)
heappush(q, a)
for i in range(k, n):
    heappush(q, p[i])
    heappop(q)
    a = heappop(q)
    print(a)
    heappush(q, a)