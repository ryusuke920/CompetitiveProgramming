n = int(input())
f = list(map(int,input().split()))
mod = 998244353
par = [i for i in range(n)]
ans = n # すべてを満たす設定にしておく

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
    if par[x] != par[y]:
        global ans
        ans -= 1
    par[x] = y

for i in range(n):
    if i != f[i] - 1:
        unite(i, f[i] - 1)

num = 2 ** ans - 1
print(num % mod)