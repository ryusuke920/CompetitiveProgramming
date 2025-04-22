Q = int(input())
from collections import deque
q = deque()
for _ in range(Q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        q.append(a[1])
    else:
        print(q.popleft())
