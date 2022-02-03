n = int(input())
import math
ans = (-1 + math.sqrt(1+8*n))/2
if ans == int(ans):
    print(ans)
else:
    print(-1)