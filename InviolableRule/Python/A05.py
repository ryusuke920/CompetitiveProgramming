n, k = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        l = k - (i + j)
        if 1 <= l <= n:
            ans += 1
    
print(ans)