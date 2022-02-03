n = int(input())
c = list(map(int,input().split()))
c.sort()
ans = 1
mod = 10 ** 9 + 7
cnt = 0
for i in range(n):
    #print("iのうえ", c[i] - cnt)
    if cnt < c[i]:
        ans *= (c[i] - cnt)
        ans %= mod
        cnt += 1
    else:
        exit(print(0))
    #print(i, ans, cnt) 
print(ans % mod)