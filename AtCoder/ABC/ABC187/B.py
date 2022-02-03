n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int,input().split())
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if -1 <= (y[j]- y[i]) /(x[j] - x[i]) <= 1:
            ans += 1
print(ans)