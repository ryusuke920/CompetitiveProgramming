n,m,x = map(int,input().split())
a = list(map(int,input().split()))
ans1 = 0
ans2 = 0
for i in range(m):
    if a[i] < x:
        ans1 += 1
    else:
        ans2 += 1
print(min(ans1,ans2))