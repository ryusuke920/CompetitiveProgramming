n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    ch = 0
    num = 1/n
    while i < k:
        i *= 2
        ch += 1
        num = (1/n)*(1/2)**ch
    ans += num
print(ans)