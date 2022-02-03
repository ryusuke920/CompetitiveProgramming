from heapq import heappop, heappush
q = []
num = 0
for i in range(int(input())):
    t = list(map(int,input().split()))
    if t[0] == 1:
        heappush(q, t[1] - num)
    elif t[0] == 2:
        num += t[1]
    elif t[0] == 3:
        ans = heappop(q)
        print(ans + num)