n, x = map(int,input().split())
ans = 0
for i in range(n):
    v, p = map(int,input().split())
    ans += v * p
    if ans > x * 100: exit(print(i + 1))

print(-1)