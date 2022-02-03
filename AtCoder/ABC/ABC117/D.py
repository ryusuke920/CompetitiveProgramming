# ２進数 -> 10進数への変換
def BinaryToDecimal(num):
    num = str(num)[::-1]
    decimal_number = 0
    for i in range(len(num)):
        decimal_number += int(num[i]) * (2 ** i)
    return decimal_number

n, k = map(int,input().split())
a = list(map(int,input().split()))
if k == 0:
    exit(print(sum(a)))
ma = bin(k)[2:]
l = len(ma)
cnt = [0] * l # 各桁ごとの1の個数
for i in range(n):
    num = bin(a[i])[2:]
    num = "0" * max(0, l - len(num)) + num
    num = list(map(int, num))
    for j in range(l):
        cnt[j] += num[j]

#print(cnt)
ans = 0
keta = 0
for i in range(l):
    a = 2 ** (l - i - 1) * (l - cnt[i]) # ansを1にする場合
    b = 2 ** (l - i - 1) * cnt[i] # ansを0にする場合
    bin_a = 2 ** (l - i - 1)
    if b >= a:
        ans += b
    elif b < a:
        if keta + bin_a <= k:
            ans += a
            keta += bin_a
        else:
            ans += b
    #print(a, b, bin_a)
print(ans)