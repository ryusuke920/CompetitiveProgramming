def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i + 1 for i, j in enumerate(sorted(set(A)))}
    return B

n, k = map(int,input().split())
c = list(map(int,input().split()))
p = list(map(int,input().split()))

if len(set(c)) < k:
    exit(print(-1))

from collections import defaultdict
d = defaultdict(int)
for i in range(n):
    if d[c[i]] == 0:
        d[c[i]] = p[i]
    else:
        d[c[i]] = min(d[c[i]], p[i])

ans = 0
for num, (i, j) in enumerate(sorted(d.items(), key=lambda x: x[1])):
    if num == k:
        exit(print(ans))
    ans += j

print(ans)