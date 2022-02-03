n = int(input())
d = {"B": 0, "W": 1, "R": 2}
COLOR = "BWR"
color = [d[i] for i in input()]

ans, nCk, mod, three = 0, 1, 3, 0 
for i, j in enumerate(color):
    if three == 0:
        ans += nCk * j

    x = n - i - 1
    y = i + 1

    if x == 0:
        break
    
    while x % mod == 0:
        x //= 3
        three += 1
    nCk *= x

    while y % mod == 0:
        y //= 3
        three -= 1
    nCk *= y
    nCk %= mod

ans %= 3
if n % 2 == 1:
    print(COLOR[ans])
else:
    print(COLOR[-ans % 3])