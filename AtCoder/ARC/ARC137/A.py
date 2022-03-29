from math import gcd
l, r = map(int, input().split())

ans = 0
for R in reversed(range(r - 2000, r + 1)):
    for L in range(l, l + 2000):
        if R <= L: continue
        if gcd(L, R) == 1:
            ans = max(ans, R - L)

print(ans)