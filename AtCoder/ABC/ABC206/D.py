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

n = int(input())
a = list(map(int,input().split()))
par = [i for i in range(max(a))]

for i in range(n // 2):
    if a[i] != a[-1 - i]:
        unite(a[i] - 1, a[-1 -i] - 1)

num = [0] * (max(a))
for i in range(max(a)):
    num[find(i)] += 1

print(sum(max(0, i - 1) for i in num))