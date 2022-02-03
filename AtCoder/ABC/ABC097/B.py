x = int(input())
ans = 1
for i in range(2,1000):
    tmp = 2
    while i**tmp <= x:
        ans = max(ans,i**tmp)
        tmp += 1
print(ans)