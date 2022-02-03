N = int(input())
ans = 0
n = 0
while n * (n + 1) <= 2 * N + 2:
    if n != 0:
        a = (2 * N - n ** 2 + n) / (2 * n)
        a = int(a)
    else:
        a = (-1 + (n ** 2 + 4 * N)**0.5) / 2
        a = int(a)
    if n * (2 * a + (n - 1)) == 2 * N and n >= 0:
        ans += 1
    n += 1
print(ans * 2)