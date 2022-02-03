from itertools import product
n = int(input())
f = [list(map(int,input().split())) for _ in range(n)]
p = [list(map(int,input().split())) for _ in range(n)]

ans = -10 ** 18
for i in product([0, 1], repeat=10):
    if i.count(0) == 10: continue

    is_open = [0] * n
    for j in range(n):
        for k in range(10):
            if i[k] == 1 and f[j][k] == 1:
                is_open[j] += 1
    plus = []
    for j in range(n):
        plus.append(p[j][is_open[j]])
    
    ans = max(ans, sum(plus))

print(ans)