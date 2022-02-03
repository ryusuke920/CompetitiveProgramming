n,q = map(int,input().split())
cnt = [0]*n
#いもす法
for i in range(q):
    l,r = map(int,input().split())
    cnt[l-1] += 1
    if r < n:
        cnt[r] -= 1
for i in range(n-1):
    cnt[i+1] += cnt[i]
    cnt[i] %= 2
cnt[n-1] %= 2

ans = ""
for i in range(n):
    if cnt[i]%2 == 0:
        ans += "".join("0")
    else:
        ans += "".join("1")
print(ans)