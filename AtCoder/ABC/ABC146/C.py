a,b,x = map(int,input().split())
l,r = 1,10**9
while l <= r:
    mid = (l+r)//2
    if a*mid + b*len(str(mid)) > x:
        r = mid-1
    else:
        l = mid+1
print(l-1)