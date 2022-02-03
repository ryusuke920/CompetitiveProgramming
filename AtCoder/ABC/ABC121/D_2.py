"""
２進数に直した際の i 桁目 (i >= 1) について
周期：2 ** i
余り：r = n % (2 ** i)
セット数：p = n // (2 ** i)
１セットに含まれる１の個数：p * 2 ** (i - 1)
余り内の１の個数：max(r % 2 ** (i - 1), 0)
合計数 mod2 の値に 2 ** i
"""

n = int(input())
n += 1
ans = 0
i = 1
while True:
    p = n // (2 ** i)
    r = n % (2 ** i)
    p_ko = p * (2 ** (i - 1))
    # r_ko = max(r, 2 ** (i - 1)) - 2 ** (i - 1)
    r_ko = max(r - 2 ** (i - 1), 0)
    num = p_ko + r_ko
    num %= 2
    ans += num * (2 ** i)
    print(F"i={i}, ans={ans}, num={num}, p={p}, r={r}, p_ko={p_ko}, r_ko={r_ko}")

    if 2 ** i > n:
        break

    i += 1

print(ans)
print(bin(ans))