def f(a: int, b: int) -> int:
    return a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3

n = int(input())
ans = 10 ** 18
b = 10 ** 6
for a in range(10 ** 6 + 1):
    while f(a, b) >= n and b >= 0:
        ans = min(ans, f(a, b))
        b -= 1

print(ans)