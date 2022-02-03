n,m = map(int,input().split())
ans = [0]*m
py = [[] for _ in range(n)]
for i in range(m):
    p,y = map(int,input().split())
    py[p-1].append((y,i))

for i,j in enumerate(py):
    j.sort()
    for k, (l,m) in enumerate(j):
        ans[m] = "%06d%06d" %(i+1,k+1)

for i in ans:
    print(i)