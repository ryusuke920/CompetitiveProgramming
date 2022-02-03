#n = int(input())
n, d, h = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = -10 ** 18
for i in range(n):
    a, b = map(int,input().split())
    if d - a == 0:
        ans = max(ans, h)
    else:
        u = h - (h - b) / (d - a) * d
        ans = max(ans, u)

if ans <= 0:
    print(0)
else:
    print(ans)