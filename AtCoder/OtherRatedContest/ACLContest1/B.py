from itertools import product
n = int(input())
if n == 1:
    exit(print(1))
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

def extgcd(a: int, b: int) -> list:
    "ax + by = gcd(a,b) = d となる (x, y, d) を返す"
    if b == 0:
        return (1, 0, a)

    q, r = a // b, a % b
    x, y, d = extgcd(b, r)
    s, t = y, x - q * y

    return [s, t, d] # (qb + r)s + bt = dとなる s, t, d

X = factorization(2 * n)
ans = []
for i in product([0, 1], repeat = len(X)):
    num_a, num_b = [], [] # K, K + 1
    for j in range(len(X)): # 各素因数をどっちに振り分けるか
        if i[j] == 1:
            num_a.append(X[j][0] ** X[j][1])
        else:
            num_b.append(X[j][0] ** X[j][1])

    seki_a = seki_b = 1
    for i in range(len(num_a)):
        seki_a *= num_a[i]
    for i in range(len(num_b)):
        seki_b *= num_b[i]
    

    cnt = extgcd(seki_a, seki_b)
    R = 0 + seki_a * ((-1 - 0) // cnt[2]) * cnt[0]
    ans.append(R)

ANS = []
for i in range(len(ans)):
    if ans[i] <= 0: continue
    ANS.append(ans[i])

ANS.sort()
print(min(ANS))