x, y = map(int,input().split())
if (x + y) % 3 != 0:
    exit(print(0))
# (i + 1, j + 2) = n,  (i + 2, j + 1) = m とすると、

# n + 2m = x
# 2n + m = y

# 3m = 2x - y, m = (2x - y) / 3
# -3n = x - 2y, n = (2y - x) / 3
n = (2 * y - x) // 3
m = (2 * x - y) // 3
if n < 0 or m < 0:
    exit(print(0))

# n + m C n = (n + m)! / m! * n!
mod = 10 ** 9 + 7
def nCk(n, k, mod):
    num = 1
    for i in range(n - k + 1, n + 1):
        num *= i
        num %= mod
    
    for i in range(1, k + 1):
        num *= pow(i, mod - 2, mod)
        num %= mod
    return num

print(nCk(n + m, min(n, m), mod))