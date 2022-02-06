from collections import defaultdict

n = int(input())
abt = [list(map(int, input().split())) for _ in range(n)]

d = defaultdict(int)
for i in range(n):
    # 青の時のカウントをする
    if abt[i][0] == 1:
        d[abt[i][2] - abt[i][1]] += 1

ans = 0
for i in range(n):
    # 重なる赤を見つける
    if abt[i][0] == 0:
        ans += d[abt[i][2] - abt[i][1]]

print(ans)