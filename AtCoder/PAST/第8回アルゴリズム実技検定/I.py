from heapq import heappush, heappop, heapify
n = int(input())
a = list(map(int,input().split()))
num = 0
b = []
for i in a:
    t = i
    while True:
        if t % 2: break
        num += 1
        t //= 2
    b.append(t)

q = []
heapify(q)
for i in b:
    heappush(q, i)

for _ in range(num):
    mi = heappop(q)
    mi *= 3
    heappush(q, mi)

print(heappop(q))