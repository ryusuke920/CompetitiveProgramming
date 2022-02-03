n = int(input())
ans = 0
for _ in range(n):
    a,b = map(int,input().split())
    ans = max(ans,a+b)
print(ans)