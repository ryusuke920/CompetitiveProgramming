s = [input() for _ in range(3)]
for i in range(3):
    for j in range(3):
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            y = dy + i
            x = dx + j
            if not (0 <= x < 3 and 0 <= y < 3):
                continue
            if s[i][j] == s[y][x]:
                exit(print('No'))

print('Yes')