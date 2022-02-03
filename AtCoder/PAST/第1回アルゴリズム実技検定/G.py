from itertools import product, combinations
n = int(input())
a = []
for i in range(n - 1):
    a.append(list(map(int,input().split())))

ans = -10 ** 18

# ３つのグループに分ける場合
for i in product([0, 1, 2], repeat = n):

    team_1 = []
    team_2 = []
    team_3 = []
    # 3グループに分ける
    for j in range(n):
        if i[j] == 0:
            team_1.append(j)
        elif i[j] == 1:
            team_2.append(j)
        elif i[j] == 2:
            team_3.append(j)

    score = 0
    if len(team_1) >= 2:
        for k in combinations(team_1, 2):
            k = sorted(list(k))
            score += a[k[0]][k[1] - (k[0] + 1)]
    if len(team_2) >= 2:
        for k in combinations(team_2, 2):
            k = sorted(list(k))
            score += a[k[0]][k[1] - (k[0] + 1)]
    if len(team_3) >= 2:
        for k in combinations(team_3, 2):
            k = sorted(list(k))
            score += a[k[0]][k[1] - (k[0] + 1)]

    ans = max(ans, score)

print(ans)