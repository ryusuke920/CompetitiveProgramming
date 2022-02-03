h, w, k = map(int,input().split())
s = [list(input()) for _ in range(h)]

ans = [[0] * w for _ in range(h)]
now_number = 1

for i in range(h):
    berry = 0 # i列目に何個イチゴがあるか
    berry_place = [] # イチゴがi行○行目にあるか
    for j in range(w):
        if s[i][j] == "#":
            berry += 1
            berry_place.append(j)
    
    if berry == 0: continue
    already_berry = 0 # すでに見たイチゴの個数
    for j in range(w):
        ans[i][j] = now_number
        if s[i][j] == "#":
            if already_berry == berry - 1: continue
            already_berry += 1
            now_number += 1
    now_number += 1



for i in range(h):
    if ans[i][0] != 0:
        first = i # 最初に塗ってある列どこか
        break

# 最初なら上から順に見ていけば良い
if first == 0:
    for i in range(h - 1):
        if ans[i + 1][0] == 0:
            for j in range(w):
                ans[i + 1][j] = ans[i][j]
else: # ０以外なら下から順に見ていくイメージ
    for i in range(first):
        for j in range(w):
            ans[first - 1 - i][j] = ans[first - i][j]

# 再度上から順に見ていく（０行目は必ず塗ってある）
for i in range(h):
    if ans[i][0] == 0:
        for j in range(w):
            ans[i][j] = ans[i - 1][j]

for i in range(h):
    print(*ans[i])