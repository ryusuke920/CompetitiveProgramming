n,k = map(int,input().split())
ans = 0
a = [int(input()) for i in range(n)]
if n == 1:
    print(0)
    exit()

for i in range(n-3):
    if abs(a[i] - a[i+1]) <= k:
        ans += 1
    else:
        if abs(a[i]-a[i+2]) <= abs(a[i+1]-a[i+2]):
            a[i+1] = a[i]

if n >= 3:
    if abs(a[-3]-a[-2]) <= k:
        ans += 1
    else:
        if abs(a[-3]-a[-1]) <= abs(a[-2]-a[-1]):
            a[-2] = a[-3]
if n != 1:
    if abs(a[-1]-a[-2]) <= k:
        ans += 1

if ans == 0:
    print(0)
else:
    print(ans+1)