import math
n = int(input())
t = [int(input()) for _ in range(n)]
ans = t[0]
for i in range(n-1):
    ch = math.gcd(t[i+1],ans)
    ans = ans*t[i+1]//ch
print(ans)