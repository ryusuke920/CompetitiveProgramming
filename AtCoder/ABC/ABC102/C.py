n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    a[i] -= i+1
a.sort()
if n%2 == 1:
    mid = a[n//2]
else:
    mid = (a[(n-1)//2]+a[n//2])//2

ans = 0
for i in range(n):
    ans += abs(mid-a[i])
print(ans)