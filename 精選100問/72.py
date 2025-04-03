w, h = map(int,input().split())
mod = 10 ** 9 + 7
num = 1 # (w + h)!の計算をするもの
a = 1 # w!の計算をするもの
b = 1 # h!の計算をするもの

for i in range(2, w + h - 1):
    num *= i
    num %= mod

for i in range(2, w):
    a *= i
    a %= mod

for i in range(2, h):
    b *= i
    b %= mod

print(num,a,b)
print(num // (a * b) % mod)