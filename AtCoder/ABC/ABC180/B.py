n = int(input())
#x,y = map(int,input().split())
x = list(map(int,input().split()))
ans1 = 0
ans2 = 0
ans3 = 0
cnt = 0
for i in range(n):
    ans1 += abs(x[i])
    ans2 += abs(x[i])**2
    ans3 = max(ans3,abs(x[i]))
import math
print(ans1)
print(math.sqrt(ans2))
print(ans3)