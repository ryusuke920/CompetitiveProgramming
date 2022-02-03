import math
n = int(input())
x = ((-1+(math.sqrt(9+8*n)))/2) 
x = math.floor(x)
ans = 0
for i in range(3):
    if (x+i-1)*(x+i)//2 <= n+1:
        ans = max(ans,x+i-1)
print(n - ans + 1)