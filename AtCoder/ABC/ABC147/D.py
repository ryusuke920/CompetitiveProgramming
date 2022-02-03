n = int(input())
a = list(map(int,input().split()))

# 10進数 -> 2進数への変換
def DeciamlToBinary(num):
    binary_number = ""
    while num > 0:
        binary_number += str(num % 2)
        num //= 2
    if binary_number == "":
        return 0
    else:
        return int(binary_number[::-1])

le = 0
A = [] # 2進数に変換したやつを入れるところ
for i in range(n):
    x = DeciamlToBinary(a[i])
    x = str(x)
    A.append(x)
    le = max(le, len(x))

# 長さをmaxのやつに合わせる
for i in range(n):
    A[i] = A[i][::-1]
    A[i] += "0" * (le - len(A[i]))

zero = [0] * le
one = [0] * le
ans = 0
mod = 10 ** 9 + 7
for i in range(len(A)):
    for j, k in enumerate(A[i]):
        if str(k) == "0":
            zero[j] += 1
        else:
            one[j] += 1

for i in range(le):
    ans += (zero[i] * one[i]) * 2 ** i
    ans %= mod
print(ans % mod)