# nCk.pyよりも高速かな？（powを外に出した）
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

n, k = map(int,input().split())
print(combination(n, k % n)) if n <= k else print(combination(n + k - 1, k))