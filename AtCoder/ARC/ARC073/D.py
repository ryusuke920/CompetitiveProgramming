n, w = map(int, input().split())
v = [[] for _ in range(4)]

for i in range(n):
    a, b = map(int, input().split())
    if i == 0:
        p = a # 基準となるw1の重さ
    diff = a - p
    v[diff].append(b)

for i in range(4):
    v[i].sort(reverse=True)

l = [len(v[i]) for i in range(4)]
wa = [[0] for _ in range(4)]
for i in range(4):
    for j in range(l[i]):
        wa[i].append(wa[i][-1] + v[i][j])

ans = 0
for a in range(l[0] + 1):
    for b in range(l[1] + 1):
        for c in range(l[2] + 1):
            for d in range(l[3] + 1):
                weight = a * p + b * (p + 1) + c * (p + 2) + d * (p + 3)
                if weight > w: continue
                cnt = wa[0][a] + wa[1][b] + wa[2][c] + wa[3][d]
                ans = max(ans, cnt)

print(ans)