import itertools
n,m = map(int,input().split())
comb = []
for i in range(m):
    x,y = map(int,input().split())
    comb.append((x-1,y-1))

ans = 1
for i in range(1,n+1):
    for j in itertools.combinations(range(n),i):
        if all((x, y) in comb for x, y in itertools.combinations(j, 2)):
            ans = i
print(ans)