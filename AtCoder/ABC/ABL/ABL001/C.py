n,m = map(int,input().split())
par = [i for i in range(n+1)]

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x]) #経路圧縮？
        return par[x]

def same(x,y):
    return find(x) == find(y) # Boolでreturn

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[min(x,y)] = par[max(x,y)]

ans = 0
for i in range(m):
    a,b = map(int,input().split())
    unite(a,b)

for i in range(n+1):
    find(i)
par = par[1:]
ans = 0
from collections import Counter
t = Counter(par)
#print(t)
print(t.most_common()[0][1])