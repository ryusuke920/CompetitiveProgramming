from collections import defaultdict
dc = defaultdict(int)
d = defaultdict(int)
n, q = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    dc[a[i]] += 1
    d[f'{a[i]}_{dc[a[i]]}'] = i + 1

for i in range(q):
    x, k = map(int, input().split())
    if d[f'{x}_{k}'] == 0:
        print(-1)
    else:
        print(d[f'{x}_{k}'])