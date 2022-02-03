n,k = map(int,input().split())
a = list(map(int,input().split()))
ans1 = ans2 = 0
for i in range(n-1):
    for j in range(i+1,n):
        if a[i] > a[j]:
            ans1 += 1
mod = 10**9 + 7
for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            ans2 += 1
print((ans1*k + k*(k-1)*ans2//2)%mod)