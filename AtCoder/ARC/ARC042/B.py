import math
X, Y = map(int,input().split())
n = int(input())
ans = 10 ** 9
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int,input().split())

for i in range(n - 1):
    if x[i] - x[i + 1] == 0:
        d = abs(X - x[i])
    else:
        a = (y[i] - y[i + 1]) / (x[i] - x[i + 1])
        b = (x[i] * y[i + 1] - x[i + 1] * y[i]) / (x[i] - x[i + 1])
        d = (abs(a * X - Y + b)) / (math.sqrt(a ** 2 + 1))
    ans = min(d, ans)

# 最初と最後の直線と点の距離
if x[-1] - x[0] == 0:
    d = abs(X - x[-1])
else:
    a = (y[-1] - y[0]) / (x[-1] - x[0])
    b = (x[-1] * y[0] - x[0] * y[-1]) / (x[-1] - x[0])
    d = (abs(a * X - Y + b)) / (math.sqrt(a ** 2 + 1))

ans = min(d, ans)

print(ans)