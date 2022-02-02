n, m = map(int, input().split())
p = list(map(int, input().split()))
abc = [tuple(map(int ,input().split())) for _ in range(n - 1)]

num = [0] * (n + 1)
for i in range(m - 1):
    x, y = p[i], p[i + 1]

    if x > y: x, y = y, x

    # いもす法
    num[x - 1] += 1
    num[y - 1] -= 1

for i in range(n):
    num[i + 1] += num[i]

print(sum([max(0, min(abc[i][0] * num[i], abc[i][1] * num[i] + abc[i][2])) for i in range(n - 1)]))