import math
n = int(input())
r = [int(input()) for i in range(n)]
pi = math.acos(-1.0)
ans = 0
r.sort()
for i in range(n,0,-1):
    ans += (-1)**(i)*r[i-1]*r[i-1]
if n%2 == 1:
    print(ans * pi * (-1))
else:
    print(ans * pi)