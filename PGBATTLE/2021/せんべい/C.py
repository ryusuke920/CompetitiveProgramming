n = int(input())
a = list(map(int,input().split()))

from collections import defaultdict
d = defaultdict(int)
for i in a:
    d[i] += 1

if d[1] != 1:
    exit(print(-1))

for i in range(n):
    if d[2 ** (i + 1)] == 2 ** i: continue
    exit(print(-1))

ans = [0] * 2 ** n
i = 0
for rank in reversed(range(n + 1)):
    t = 2 ** rank # 探すレート帯
    now = 2 ** i - 1
    for index, result in enumerate(a):
        if result == t:
            ans[now] = index + 1
            now += 2 ** (i + 1)
    i += 1

print(*ans)