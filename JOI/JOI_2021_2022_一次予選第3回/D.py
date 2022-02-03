from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(int)
# d[i] = j := ボールiが箱jに入っている
for i in range(n):
    d[i + 1] = i + 1

for _ in range(m):
    x, y = map(int, input().split())
    for i, j in d.items():
        if i == x:
            d[i] = y
            break

for k, v in d.items():
    print(d[k])