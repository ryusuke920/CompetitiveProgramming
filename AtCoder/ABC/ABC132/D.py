def combination(n, k):
    nCk = under = top = 1
    

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

mod = 10 ** 9 + 7
n, k = map(int,input().split())
for i in range(k):
    a = combination(n - k + 1, i + 1)
    b = combination(k - 1, i)
    print(a * b % mod)