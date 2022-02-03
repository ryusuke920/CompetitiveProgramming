n = int(input())
s = [list(input()) for _ in range(n)]
d = ((1, -1), (1, 0), (1, 1))
for i in reversed(range(n - 1)):
    for j in range(2 * n - 1):
        if s[i][j] != "#": continue
        cnt = 0
        for dy, dx in d:
            y = i + dy
            x = j + dx
            if not (0 <= x < 2 * n - 1 and 0 <= y < n): continue
            if s[y][x] == "X":
                cnt += 1
        if cnt >= 1:
            s[i][j] = "X"

for i in range(n):
    print(*s[i], sep="")