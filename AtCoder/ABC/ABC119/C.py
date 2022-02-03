from itertools import product
n, a, b, c = map(int,input().split())
l = [int(input()) for _ in range(n)]

ans = 10 ** 18
for i in product([0, 1, 2, 3], repeat=n):
    x, y, z, = [], [], []
    for j in range(n):
        if i[j] == 0: continue
        if i[j] == 1: x.append(l[j])
        if i[j] == 2: y.append(l[j])
        if i[j] == 3: z.append(l[j])

    if len(x) == 0: continue
    if len(y) == 0: continue
    if len(z) == 0: continue

    num = 0
    num += abs(sum(x) - a) + (len(x) - 1) * 10
    num += abs(sum(y) - b) + (len(y) - 1) * 10
    num += abs(sum(z) - c) + (len(z) - 1) * 10

    ans = min(ans, num)

print(ans)