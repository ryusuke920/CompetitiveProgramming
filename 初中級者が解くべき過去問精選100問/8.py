n = int(input())
a = [0]*n
b = [0]*n
ans = cnta = cntb = 0
for i in range(n):
    a[i], b[i] = map(int,input().split())
a.sort()
b.sort()
if n%2 == 0:
    cnta += (a[n//2]+a[n//2-1])//2
    cntb += (b[n//2]+b[n//2-1])//2
else:
    cnta += a[n//2]
    cntb += b[n//2]
for i in range(n):
    ans += abs(a[i]-cnta) + abs(b[i]-a[i]) + abs(b[i]-cntb)
print(ans)