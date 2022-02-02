n = int(input())
c = list(map(int, input().split()))

mod = 10 ** 9 + 7

# 階乗テーブル
fac = [1] * (n + 1)
for i in range(n):
    fac[i + 1] = fac[i] * (i + 1) 
    fac[i + 1] %= mod

# 10^kの和
t = (pow(10, n, mod) - 1) * pow(9, -1, mod)

# i * Ci の和
i_Ci = 0
for i in range(9):
    i_Ci += (i + 1) * c[i]

# 1 / (c1! * c2! * ... * c9!) の積
fac_Ci = 1
for i in range(9):
    if fac[c[i]] == 0: continue
    fac_Ci *= pow(fac[c[i]], -1, mod)

ans = t * i_Ci * fac_Ci * fac[n - 1] % mod

print(ans)