from itertools import combinations
n,m = map(int,input().split())
xy = [list(map(int,input().split())) for _ in range(m)]
ans = 1
for i in range(n):
    for j in combinations(range(n),i+1):
        if all([x+1, y+1] in xy for x, y in combinations(j,2)):
            ans = i+1
print(ans)