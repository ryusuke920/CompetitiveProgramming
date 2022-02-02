n,m = map(int,input().split())
a = [0]*m
b = [0]*m
for i in range(m):
    a[i],b[i] = map(int,input().split())
par = [i for i in range(n+1)]
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
        x,y = y,x
    par[x] = y
for i in range(m):
    if b[i] > a[i]:
        a[i], b[i] = b[i], a[i]
    unite(a[i-1],b[i-1])
print(par)
