n,x = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
    a[i] = abs(x-a[i])

import math
ans = a[0]
for i in range(n-1):
    ans = math.gcd(ans,a[i+1])
print(ans)