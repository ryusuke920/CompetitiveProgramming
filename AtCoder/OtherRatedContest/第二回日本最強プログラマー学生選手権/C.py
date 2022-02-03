import math
a, b = map(int,input().split())
ans = 0
for i in range(1,b + 1):
    if a <= i * math.ceil(a / i) <= b and a <= i * math.ceil(a / i) + i <= b:
        ans = i
print(ans)