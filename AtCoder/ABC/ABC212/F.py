n = int(input())
mod = 998244353
for i in range(n):
    print(f"{i}の逆げn {pow(i, mod - 2, mod)}")
    