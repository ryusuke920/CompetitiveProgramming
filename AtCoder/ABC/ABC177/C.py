n = int(input())
a = list(map(int,input().split()))
ans = 0
mod = 10**9 + 7
num = sum(a)%mod
for i in range(n-1):
    num -= a[i]
    num %= mod
    ans += a[i]*num
    ans %= mod
print(ans)
#ポイント　sumはfor文の中にあまり入れない方がいい？（TLEになった　2020/08/30/00:37:56）