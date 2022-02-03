def combination(n, k):
    nCk = under = top = 1
    mod = 10 ** 9 + 7

    # 分母
    for i in range(2, k + 1):
        under *= i
        under %= mod

    # 分子
    for i in range(k):
        top *= (n - i)
        top %= mod

    nCk = top * pow(under, mod - 2, mod)

    return nCk % mod

n, m, k = map(int,input().split())
whole = combination(n + m, n)
r = combination(n + m, m + k + 1)
if n > m + k:
    print(0)
else:
    print((whole - r) % (10 ** 9 + 7))