import sys
input = sys.stdin.readline
v, e = map(int,input().split())
d = [[0] * v for _ in range(v)]
for i in range(v):
    for j in range(v):
        if i == j:
            d[i][j] = 0
        else:
            d[i][j] = 10 ** 18

for i in range(e):
    s, t, dist = map(int,input().split())
    d[s][t] = dist

for k in range(v):
    for i in range(v):
        for j in range(v):
            if d[i][k] == 10 ** 18 or d[k][j] == 10 * 18: continue
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

#print(*d, sep = "\n")

for i in range(v):
    if sum(d[i]) < 0:
        exit(print("NEGATIVE CYCLE"))

for i in range(v):
    ans = ""
    for j in range(v):
        if j == v - 1:
            if d[i][j] == 10 ** 18:
                ans += "INF"
            else:
                ans += str(d[i][j]) + ""
        else:
            if d[i][j] == 10 ** 18:
                ans += "INF "
            else:
                ans += str(d[i][j]) + " "
    print(ans)