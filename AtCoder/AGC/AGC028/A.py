n,m = map(int,input().split())
s = input()
t = input()
import math
st = math.gcd(n,m)
for i in range(st):
    if s[n//st*i] != t[m//st*i]:
        exit(print(-1))
print(n*m//st)