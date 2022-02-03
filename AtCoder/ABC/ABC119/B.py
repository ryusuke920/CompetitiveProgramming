n = int(input())
ans = 0
for i in range(n):
    x,u = map(str,input().split())
    x = float(x)
    if u == "JPY":
        ans += x
    else:
        ans += 380000*x
print(ans)