n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 10 ** 18
for i in range(n - 1):
    for j in range(i + 1, n):
        ans = min(ans, ((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) ** 0.5)

print(ans)