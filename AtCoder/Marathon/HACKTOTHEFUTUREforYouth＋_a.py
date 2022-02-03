n, k, B = map(int,input().split()) # マスの大きさ・印の総数・ポリオミノの種類数
pori = [list(map(int,input().split())) for _ in range(k)] # 縦・横
pori.sort(key=lambda x: (x[1], x[0]))
#print(*pori, sep="\n")
for i in range(B):
    a, b, c = map(int,input().split())
    s = [list(input()) for _ in range(a)]

ans = []
for i in range(k - 1):
    x, y = pori[i][1], pori[i][0]
    nx, ny = pori[i + 1][1], pori[i + 1][0]

    # 縦を塗る
    for j in range(min(y, ny), max(y, ny) + 1):
        if (1, j, min(x, nx)) not in ans:
            ans.append((1, j, min(x, nx)))

    # 横を塗る
    for j in range(min(x, nx), max(x, nx) + 1):
        if (1, max(y, ny), j) not in ans:
            ans.append((1, max(y, ny), j))
        if (1, min(y, ny), j) not in ans:
            ans.append((1, min(y, ny), j))

D = (
    (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2),
    (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
    (0, -2), (0, -1), (0, 1), (0, 2),
    (1, -2), (1, -1), (1, 0), (1, 1), (1, 2),
    (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)
)

d = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1))

for i in range(n):
    for j in range(n):
        cnt = 0
        if (1, j, i) not in ans: continue
        for dy, dx in D:
            y = i + dy
            x = j + dx
            if not (0 <= y < n and 0 <= x < n): break
            if (1, x, y) in ans:
                cnt += 1
        if cnt == 24:
            if [i, j] not in pori:
                for dy, dx in d:
                    y = i + dy
                    x = j + dx
                    ans.remove((1, x, y))
                ans.remove((1, j, i))

for i in range(n):
    for j in range(n):
        if (1, j, i) not in ans: continue
        if [i, j] in pori: continue
        cnt = 0
        for dy, dx in d:
            y = i + dy
            x = j + dx
            if not (0 <= y < n and 0 <= x < n): continue
            if [1, x, y] in ans:
                cnt += 1
        if cnt == 8:
            if [i, j] not in pori:
                ans.remove((1, j, i))

print(len(ans))
for i in ans: print(*i)