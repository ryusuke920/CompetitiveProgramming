n = int(input())
#a,b = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
cnt = 0
import math

if n == 1:
    print(a[0])
else:
    ans = math.gcd(a[0],a[1])
    for i in range(n-2):
        ans = math.gcd(ans,a[i+2])
    print(ans)