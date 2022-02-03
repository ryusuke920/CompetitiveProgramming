n,l = map(int,input().split())
ans = 0 
for i in range(l,n+l):
    ans += i
if l <= 0 and n+l > 0:
    print(ans)
elif l <= 0 and n+l <= 0:
    print(ans - (n+l)+1)
else:
    print(ans-l)