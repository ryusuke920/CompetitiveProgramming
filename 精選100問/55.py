from collections import deque
from bisect import bisect_left
n = int(input())
a = [int(input()) for _ in range(n)]

q = deque([a[0]])
for i in range(n - 1):
    x = bisect_left(q, a[i + 1])
    if x == 0:
        q.appendleft(a[i + 1])
    else:
        q[x - 1] = a[i + 1]

print(len(q))