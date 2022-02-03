n,m,a,b = map(int,input().split())
ans = [b]*n
for i in range(m):
    l,r = map(int,input().split())
    for j in range(l,r+1):
        ans[j-1] = a
print(sum(ans))