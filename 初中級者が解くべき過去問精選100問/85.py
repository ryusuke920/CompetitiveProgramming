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
    c, x, y = map(int,input().split())
    if c == 0:
        unite(x, y)
    elif c == 1:
        if same(x, y):
            print(1)
        else:
            print(0)