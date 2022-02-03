from math import gcd
n, k = map(int,input().split())
a = list(map(int,input().split()))
GCD = 0
for i in a:
    GCD = gcd(GCD, i)

if k <= max(a) and k % GCD == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")