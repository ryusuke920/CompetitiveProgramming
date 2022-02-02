n, s = map(int, input().split())

ans = 0
for red in range(1, n + 1):
    for blue in range(1, n + 1):
        if red + blue <= s:
            ans += 1

print(ans)