def combination(n, k):
    nCk = under = top = 1

    for i in range(2, k + 1):
        under *= i
        under %= mod

    for i in range(k):
        top *= (n - i)
        top %= mod

    nCk = top * pow(under, mod - 2, mod)

    return nCk % mod

x, y = map(int,input().split())
mod = 10 ** 9 + 7

if (x + y) % 3:
    exit(print(0))

if not ((y - 2 * x) % 3 == 0 and (x - 2 * y) % 3 == 0):
    exit(print(0))

if 2 * x - y >= 0:
    print(combination((x + y) // 3, (2 * x - y) // 3))
else:
    print(combination((x + y) // 3, (2 * y - x) // 3))