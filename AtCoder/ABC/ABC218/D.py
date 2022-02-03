def CC(A: list) -> list:
    "座標圧縮"
    B = {j: i + 1 for i, j in enumerate(sorted(set(A)))}
    return B

n = int(input())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int,input().split())

x_cc = CC([i for i in a])
y_cc = CC([i for i in b])

xy = []
for i in range(n):
    xy.append([x_cc[a[i]], y_cc[b[i]]])

ans = 0

from collections import defaultdict
d = defaultdict(int)

for i in range(n - 1):
    for j in range(i + 1, n):
        if xy[i][1] == xy[j][1]:
            d[str(xy[i][0] - 1) + "_" + str(xy[j][0] - 1)] += 1
            d[str(xy[j][0] - 1) + "_" + str(xy[i][0] - 1)] += 1
            

for i in d.values():
    cnt = max(0, i * (i - 1) // 2)
    ans += cnt
print(ans // 2)
#print(d)