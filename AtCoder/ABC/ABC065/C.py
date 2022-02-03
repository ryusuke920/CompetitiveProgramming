n,m = map(int,input().split())
import math
mod  = 10**9+7
if abs(m-n) >= 2:
    print(0)
elif abs(m-n) == 1:
    print((math.factorial(m)*math.factorial(n))%mod)
else:
    print((2*math.factorial(m)*math.factorial(n))%mod)