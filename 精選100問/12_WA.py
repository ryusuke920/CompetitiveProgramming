n,m = map(int,input().split())
par = [i for i in range(n)]
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
    par[x] = y
for i in range(m):
    x, y = map(int,input().split())
    if x > y:
        x, y = y, x
    unite(x-1, y-1)
ans = [0]*n
for i in range(n):
    ans[find(i)] += 1
print(max(ans))
print(par)
print(ans)