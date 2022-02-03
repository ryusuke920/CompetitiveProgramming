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
    nCk = under = top = 1

    for i in range(2, k + 1):
        under *= i
        under %= mod

    for i in range(k):
        top *= (n - i)
        top %= mod

    nCk = top * pow(under, mod - 2, mod)

    return nCk % mod

n, m = map(int,input().split())
num = factorization(m)
mod = 10 ** 9 + 7
ans = 1
# nHk = (n+k-1)Ck
for number, count in num:
    ans *= combination(count + (n - 1), count)
    ans %= mod

if m == 1:
    print(1)
else:
    print(ans)