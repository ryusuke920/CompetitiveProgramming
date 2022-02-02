p = int(input())
p /= 100
w = 35 * p ** 4 * (1 - p) ** 3
x = 21 * p ** 5 * (1 - p) ** 2
y = 7 * p ** 6 * (1 - p)
z = p ** 7
ans = w + x + y + z
ans *= 100
print(ans)