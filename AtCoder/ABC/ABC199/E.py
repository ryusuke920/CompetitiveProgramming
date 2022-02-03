n, m = map(int,input().split())
ans = 0
import math
if m == 0:
    exit(print(math.factorial(n)))

def combination(n, k):
    nCk = 1
    mod = 10 ** 9 + 7

    for i in range(n - k + 1, n + 1):
        nCk *= i
        nCk %= mod

    for i in range(1, k + 1):
        nCk *= pow(i, mod - 2, mod)
        nCk %= mod
    return nCk

for i in range(m):
    x, y, z = map(int,input().split())
  
    #a = math.factorial(x) #
    for z in range(0, z + 1):
        b = combination(y, z)
        #B = math.factorial(z)
        
        c = combination(n - y, x - z)
        #C = math.factorial(x - z)

        D = math.factorial(n - x)

        E = math.factorial(x)

        #ans += b*B*c*C*D
        ans += b * c *D* E
        #print(i,ans,b,c,E,z)
print(ans)