def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

n = int(input())
ans = 1
mod = 10**9 + 7
cnt = {}
for i in range(2,n+1):
    div = factorization(i)
    for j in range(len(div)):
        if div[j][0] in cnt:
            cnt[div[j][0]] += div[j][1]
        else:
            cnt[div[j][0]] = 1
for i in cnt:
    ans *= (cnt[i]+1)%mod
print(ans%mod)