n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
from bisect import bisect_left
num = [a[0]]
x = a[0]
for i in range(n-1):
    x += a[i + 1]
    num.append(x) # 累積和

cnt = 0 # 条件が厳しくなっていくのを足していく
for i in range(n):
    t = bisect_left(num, k + cnt)
    ans += max(0, n - t)
    cnt += a[i]
print(ans)