import math
n,d = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]
count = 0
for i in range(n-1):
    for j in range(i+1,n):
        ans = 0
        for k in range(d):
            ans += (x[i][k]-x[j][k])**2
        if math.sqrt(ans).is_integer() == True:
            count += 1
print(count)