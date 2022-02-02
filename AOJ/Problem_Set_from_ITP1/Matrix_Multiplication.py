n,m,l = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(m)]
c = [[0]*l for _ in range(n)]

for i in range(n):
    for j in range(l):
        num = 0
        for k in range(m):
            num += a[i][k] * b[k][j]
        c[i][j] = num

for i in range(n):
    print(*c[i])