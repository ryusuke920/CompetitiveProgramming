n = int(input())
ans = 10 ** 18

for i in range(n):
    a,p,x = map(int,input().split())
    if a < x:
        ans = min(ans, p)
if ans == 10 ** 18:
    print(-1)
else:
    print(ans)