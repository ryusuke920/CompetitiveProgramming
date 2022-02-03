n,k = map(int,input().split())
ans = 0
cnt = 0
mod = 998244353
d = [0]*2*k
for i in range(k):
    d[i*2], d[i*2+1] = map(int,input().split())
a = [0]*(n+1)
b = [0]*(n+1)
a[1] = 1
b[1] = 1
for i in range(2,n+1):
    cnt = 0
    for j in range(k):
        if i - d[2*j] > 0:
            cnt += b[i - d[2*j]]
        if i - d[2*j+1] - 1 > 0:
            cnt -= b[i-d[2*j+1] - 1]
        a[i] = cnt
        b[i] = (b[i-1]+a[i] % mod)
print(a[n]%mod)