n,x, = map(int,input().split())
a = list(map(int,input().split()))
num = a[0]
ans = 0
if num > x:
    ans += a[0] - x
    a[0] = x
for i in range(n-1):
    if a[i] + a[i+1] > x:
        ans += a[i+1]+a[i] - x
        a[i+1] = x - a[i]
print(ans)