n,a = map(int,input().split())
import math
if a == 0:
    print(0,0)
else:
    print(math.ceil(a/3),min(a,n//3))