n,m = map(int,input().split())
h = list(map(int,input().split()))
ans = [1]*n
for i in range(m):
    a,b = map(int,input().split())
    if h[a-1] > h[b-1]:
        ans[b-1] = 0
    elif h[a-1] == h[b-1]:
        ans[a-1] = ans[b-1] = 0
    else:
        ans[a-1] = 0
print(ans.count(1))