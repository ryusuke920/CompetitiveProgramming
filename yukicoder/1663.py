a, b, c, d, mod = map(int,input().split())
ans = -1
for i in range(a, b + 1):
    for j in range(c, d + 1):
        ans = max(ans, (i + j) % mod)
print(ans)