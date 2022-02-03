sx,sy,gx,gy,t,v = map(int,input().split())
n = int(input())
leng = t*v
import math
for i in range(n):
    a,b, = map(int,input().split())
    dist = math.sqrt((sx-a)**2 + (sy-b)**2) + math.sqrt((gx-a)**2 + (gy-b)**2)
    if dist <= leng:
        print("YES")
        exit()
else:
    print("NO")