n,m = map(int,input().split())
par = [i for i in range(n+1)]
a = list(map(int,input().split()))
b = list(map(int,input().split()))

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
    par[x] = y

ans = 0
for i in range(m):
    c,d = map(int,input().split())
    unite(c,d)

for i in range(n):
    find(i+1)
par = par[1:]

fact = [0]*n
ans = [0]*n
for i in range(n):
    fact[par[i]-1] += a[i]
    ans[par[i]-1] += b[i]

for i in range(len(fact)):
    if fact[i] != ans[i]:
        print("No")
        break
else:
    print("Yes")