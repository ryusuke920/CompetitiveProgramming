h, w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]

num = []

for i in range(h):
    for j in range(w):
        if i % 2 == 0: # 左から右
            if j != w - 1: # 一番恥じゃない
                if a[i][j] % 2 == 0: continue
                a[i][j] -= 1
                a[i][j + 1] += 1
                num.append([i + 1, j + 1, i + 1, j + 2])
            else: # j == w - 1
                if i != h - 1:
                    if a[i][j] % 2 == 0: continue
                    a[i][j] -= 1
                    a[i + 1][j] += 1
                    num.append([i + 1, j + 1, i + 2, j + 1])
        else: # 右から左
            if j != w - 1: # 一番恥じゃない
                if a[i][-1 - j] % 2 == 0: continue
                a[i][w - 1 - j] -= 1
                a[i][w - 1 - j - 1] += 1
                num.append([i + 1, w - j, i + 1, w - j - 1])
            else:
                if a[i][-1 - j] % 2 == 0: continue
                if i != h - 1:
                    a[i][-1 - j] -= 1
                    a[i + 1][-1 - j] += 1
                    num.append([i + 1, w - j, i + 2, w - j])

print(len(num))
for i in range(len(num)):
    print(*num[i])