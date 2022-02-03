h, w = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))
num = [[0] * 3 for _ in range(h * w)] # [x座標、y座標、その数字]
x = y = now_number = 0
for i in range(h * w):
    a[now_number] -= 1
    if y % 2 == 0: # 左から右に行く時
        num[i] = [y, x, now_number + 1]
    elif y % 2 == 1: # 右から左に行く時
        num[i] = [y, w - x, now_number + 1]
    if a[now_number] == 0:
        now_number += 1
    x += 1
    if x == w - 1:
        x = 0
        y += 1

ans = [[0] * w for _ in range(h)]

cnt = 0
for i in range(h * w):
    ans[cnt][i % w] = num[i][2]
    if i % w == (w - 1) and i != 0:
        cnt += 1

if w == 1:
    print(num[0][2])
    for i in range(h - 1):
        print(*ans[i])
else:
    for i in range(h):
        if i % 2 == 0:
            print(*ans[i])
        else:
            print(*ans[i][::-1])