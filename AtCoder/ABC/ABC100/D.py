from itertools import product
n, m = map(int,input().split())
x, y, z = [0] * n, [0] * n, [0] * n

for i in range(n):
    x[i], y[i], z[i] = map(int,input().split())

ans = 0
for i in product([-1, 1], repeat = 3):
    num = [] # 「綺麗さ」「おいしさ」「人気度」の 3つの値
    for j in range(n):
        cnt = (x[j] * i[0]) + (y[j] * i[1]) + (z[j] * i[2])
        num.append(cnt)
    num.sort(reverse = True)

    Sum = 0
    for j in range(m):
        Sum += num[j]
    
    ans = max(ans, Sum)

print(ans)