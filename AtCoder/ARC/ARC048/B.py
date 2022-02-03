n = int(input())
rh = [list(map(int, input().split())) for _ in range(n)]

# 1 > 2, 2 > 3, 3 > 1
t = 10 ** 5
wa = [0] * (t + 1)
# rate[i][j] := レートがiで出す手がjである人の人数
rate = [[0] * 3 for _ in range(t)]
for i in range(n):
    r, h = rh[i]
    wa[r] += 1
    rate[r - 1][h - 1] += 1

for i in range(t - 1):
    wa[i + 1] += wa[i]

for i in range(n):
    r, h = rh[i]
    win = wa[r - 1]
    equal = max(0, rate[r - 1][h - 1] - 1)
    
    if h == 1: # 同レート帯のチョキに勝つ
        win += rate[r - 1][1]
    elif h == 2: # 同レート帯のパーに勝つ
        win += rate[r - 1][2]
    elif h == 3: # 同レート帯のグーに勝つ
        win += rate[r - 1][0]
    
    lose = n - 1 - (win + equal)

    print(win, lose, equal)