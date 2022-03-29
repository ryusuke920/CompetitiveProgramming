from collections import deque, defaultdict

n = int(input())
start, end = map(int, input().split())
a = list(map(int, input().split()))

set_a = set()
for i in a:
    set_a.add(i)

d = defaultdict(int)
d[start] = 0

for i in a:
    d[i] = -1
d[end] = -1

q = deque([start])
while q:
    v = q.popleft()
    for i in range(30):
        num = v ^ 2 ** i
        if d[num] != -1: continue
        d[num] = d[v] + 1
        q.append(num)

print(d[end] - 1) if d[end] != -1 else print(-1)