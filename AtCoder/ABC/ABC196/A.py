a,b= map(int,input().split())
c,d= map(int,input().split())
ans = -10 ** 18
for i in range(a, b + 1):
    for j in range(c, d + 1):
        ans = max(ans, i - j)
print(ans)