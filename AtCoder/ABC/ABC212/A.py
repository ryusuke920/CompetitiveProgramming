Q = int(input())
from collections import deque
from heapq import heappop, heappush
q = []
cnt = 0
num = [0] * 10**6
for i in range(Q):
    t = list(map(int,input().split()))
    if t[0] == 1:
        cnt += 1
        heappush(q, (t[1], cnt))
    elif t[0] == 2:
        num[cnt] += t[1]
        #cnt += 1
    elif t[0] == 3:
        v = heappop(q)
        ans = v[0] + num[v[1]]
        print(ans)