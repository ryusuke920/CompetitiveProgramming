l,r = map(int,input().split())
ans = 2019
if r-l+1 >= 2019:
    print(0)
else:
    for i in range(l,r):
        for j in range(i+1,r+1):
            ans = min( (i*j) % 2019, ans)
    print(ans)