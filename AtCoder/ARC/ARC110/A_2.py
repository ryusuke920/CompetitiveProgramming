import math
n = int(input())
ans = 1
for i in range(2,n+1):
    ans = i * ans // math.gcd(ans,i)
print(ans + 1)