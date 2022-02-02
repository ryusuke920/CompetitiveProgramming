n = int(input())
a = [0]*n
b = [0]*n
for i in range(n):
    a[i], b[i] = map(int,input().split())
m = int(input())
c = [0]*m
d = [0]*m
for i in range(m):
    c[i], d[i] = map(int,input().split())
difx = [[0]*m for _ in range(n)]
dify = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        difx[i][j] = c[j]-a[i]
        dify[i][j] = d[j]-b[i]
ansx = difx[0]
ansy = dify[0]
for i in range(n-1):
    ansx = set(ansx) & set(difx[i+1])
    ansy = set(ansy) & set(dify[i+1])
ansx = list(ansx)
ansy = list(ansy)
print(*ansx, *ansy)