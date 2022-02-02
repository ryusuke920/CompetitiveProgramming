def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x,y):
    return find(x) == find(y)

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y

n, m = map(int,input().split())
par = [i for i in range(n)]
a, b = [0] * m ,[0] * m
ans = [n * (n - 1) // 2]

for i in reversed(range(m - 1)):
    unite(a[i] - 1, b[i] - 1)