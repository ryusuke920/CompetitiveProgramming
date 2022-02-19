x = int(input())

mod = 998244353
ans = 0
l = len(bin(x)[2:])

if x <= 4:
    exit(print(x))

for i in range(1, l + 2):
    two = i
    three = x - 2 * i
    if three % 3 != 0: continue
    three //= 3
    if two < 0 or three < 0: continue
    num = pow(2, two, mod) * pow(3, three, mod)
    num %= mod
    print(i,two,three, num)
    ans = max(ans, num)

print(ans)