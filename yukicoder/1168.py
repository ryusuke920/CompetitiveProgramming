# 桁の和を求める（intのまま計算するパターン）
def DigitSum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10

    return digit_sum

n = int(input())
a = [n]
for i in range(99):
    a.append(DigitSum(a[-1]))

print(a[-1])