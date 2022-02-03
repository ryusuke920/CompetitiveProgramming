n = int(input())
p = [int(input()) for _ in range(n)]
ans = [0]*n
for i in range(n):
    while p[i] %10 == 0:
        ans[i] += 1
        p[i] //= 10
print(min(ans))