n = int(input())
ans = 10**9
for i in range(1,int(n**0.5)+1):
    y = i
    x = n//y
    ch = abs(x-y) + n-(x*y)
    ans = min(ans,ch)
print(ans)