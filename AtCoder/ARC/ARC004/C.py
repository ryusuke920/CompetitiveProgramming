x, y = map(int, input().split('/'))

ans = []
for n in range(2 * x // y - 1, 2 * x // y + 2):
    if n * x % y == 0:
        m = n * (n + 1) // 2 - n * x // y
        if 1 <= m <= n:
            ans.append((n, m))

if len(ans):
    for n, m in ans:
        print(n, m)
else:
    print('Impossible')