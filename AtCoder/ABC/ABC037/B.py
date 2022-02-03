n,q = map(int,input().split())
ans = [0]*n
for i in range(q):
    l,r,t = map(int,input().split())
    for j in range(l-1,r):
        ans[j] = t
for i in range(n):
    print(ans[i])