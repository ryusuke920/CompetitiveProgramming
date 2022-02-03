from heapq import heappush, heappop
from collections import deque

q = deque()
pri_q = []

Q = int(input())
for i in range(Q):
    t = list(map(int,input().split()))
    if t[0] == 1:
        q.append(t[1])
    elif t[0] == 2:
        if len(pri_q) > 0:
            print(heappop(pri_q))
        else:
            print(q.popleft())
    elif t[0] == 3:
        for i in q:
            heappush(pri_q, i)
        q = deque()