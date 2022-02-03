def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

def combination(n, k):
    nCk = 1
    mod = 998244353

    for i in range(n - k + 1, n + 1):
        nCk *= i
        nCk %= mod

    for i in range(1, k + 1):
        nCk *= pow(i, mod - 2, mod)
        nCk %= mod
    return nCk

n, m = map(int,input().split())
mod = 998244353

ans = 0
# 末尾の数字を全探索
for i in range(2, m + 1):

    # 素因数分解
    x = factorization(i)

    cnt = 1
    num = [0] * len(x)
    for j in range(len(x)):
        # n - 2 個の柵とα^jのj個のボールを分ける組み合わせ
        num[j] = combination(max(0, (n - 1)) + x[j][1], x[j][1])
    
    for j in range(len(x)):
        cnt *= num[j]
        cnt %= mod

    ans += cnt
    ans %= mod

ans += 1
print(ans % mod)