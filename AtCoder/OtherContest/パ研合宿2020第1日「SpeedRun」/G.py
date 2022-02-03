n, m = map(int,input().split())
l = [0] * m
r = [0] * m
x = [0] * m

for i in range(m):
    l[i], r[i], x[i] = map(int,input().split())

from itertools import product
ans = -100000
for i in product([0, 1], repeat = n):
    num = [0] * n
    for j in range(n):
        if i[j] == 1:
            num[j] = 1
    ch = 0
    for k in range(m):
        if sum(num[l[k] - 1 : r[k]]) != x[k]:
            ch = 1
            break
    if ch == 0:
        ans = max(ans, sum(num))
if ans == -100000:
    print(-1)
else:
    print(ans)