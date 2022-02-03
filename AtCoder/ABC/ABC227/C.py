n = int(input())

ans = 0
for a in range(1, int(n ** (1 / 3)) + 10):
    for b in range(a, int((n / a) ** 0.5) + 10):
        ans += max(0, int(n // (a * b)) - b + 1)

print(ans)