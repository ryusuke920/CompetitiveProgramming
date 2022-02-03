import math
n = int(input())
a = list(map(int,input().split()))
ans = a[0]
for i in range(n-1):
    ans = math.gcd(ans,a[i+1])
print(ans)