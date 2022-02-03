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

n, q = map(int,input().split())
par = [i for i in range(n)]

for i in range(q):
    t, u, v = map(int,input().split())
    if t == 0:
        unite(u - 1, v - 1)
    elif t == 1:
        if same(u - 1, v - 1):
            print(1)
        else:
            print(0)