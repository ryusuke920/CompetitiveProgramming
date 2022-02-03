import math
n = int(input())
a = list(map(int,input().split()))
ans = a[0]
for i in range(1,n):
    ans = math.gcd(a[i],ans)
print(ans)