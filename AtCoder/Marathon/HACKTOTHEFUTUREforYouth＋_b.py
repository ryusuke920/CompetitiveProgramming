import sys
input = sys.stdin.readline
import random
def random_search(l: list):
    p = []
    for i, j in l:
        p.append((i, j))
    random.shuffle(p)

    ans = []
    for i in range(k - 1):
        x, y = p[i][1], p[i][0]
        nx, ny = p[i + 1][1], p[i + 1][0]

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
    
    return len(ans), ans


n, k, B = map(int,input().split()) # マスの大きさ・印の総数・ポリオミノの種類数
pori = [list(map(int,input().split())) for _ in range(k)] # 縦・横
#pori.sort(key=lambda x: (x[0], x[1]))

for i in range(B):
    a, b, c = map(int,input().split())
    s = [list(input()) for _ in range(a)]

cnt = 10 ** 18
for i in range(10):
    c = random_search(pori)
    if cnt >= c[0]:
        cnt = c[0]
        q = c[1]

print(cnt)
for i in q:
    print(*i)