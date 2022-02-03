n, m = map(int,input().split())
ans = 1
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        if i * n <= m:
            ans = max(ans, i)
        if i >= n:
            ans = max(ans, m // i)
print(ans)