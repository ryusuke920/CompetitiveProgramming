from collections import defaultdict
n = int(input())
x, y = [0] * n, [0] * n
for i in range(n):
    x[i], y[i] = map(int,input().split())

d = defaultdict(int)
for i in range(n):
    for j in range(n):
        if i == j: continue
        X = x[i] - x[j]
        Y = y[i] - y[j]
        d[X, Y] += 1

if n == 1:
    print(1)
else:
    print(n - max(d.values()))