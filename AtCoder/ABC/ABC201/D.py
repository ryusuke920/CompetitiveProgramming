import sys
input = sys.stdin.readline
import copy
h, w = map(int,input().split())
ao = ta = 0
grid = []
if h == 1 and w == 1:
    exit(print("Draw"))

for i in range(h):
    t = list(input())
    grid.append(t)

tate, yoko = [[0, 0] for _ in range(h)], [[0, 0] for _ in range(w)] # taka, aoki
for i in range(h - 1):
    tate[i + 1][0] += tate[i][0]
    tate[i + 1][1] += tate[i][1]
    if i % 2 == 1: # aoki
        if grid[i + 1][0] == "+":
            tate[i + 1][1] += 1
        else:
            tate[i + 1][1] -= 1
    else:# taka
        if grid[i + 1][0] == "+":
            tate[i + 1][0] += 1
        else:
            tate[i + 1][0] -= 1
for i in range(w - 1):
    yoko[i + 1][0] += yoko[i][0]
    yoko[i + 1][1] += yoko[i][1]
    if i % 2 == 1: # aoki
        if grid[0][i + 1] == "+":
            yoko[i + 1][1] += 1
        else:
            yoko[i + 1][1] -= 1
    else:# taka
        if grid[0][i + 1] == "+":
            yoko[i + 1][0] += 1
        else:
            yoko[i + 1][0] -= 1

ans = [[] for _ in range(h)]
for i in range(h):
    ans[i].append(tate[i])
for i in range(w - 1):
    ans[0].append(yoko[i + 1])
# 高橋：青木

for i in range(1, h):
    for j in range(1, w):
        if (i + j) % 2 == 0: # aoki
            if ans[i][j - 1][1] == ans[i - 1][j][1]:
                if ans[i][j - 1][0] > ans[i - 1][j][0]:#上の方がいい
                    cnt = copy.copy(ans[i - 1][j])
                else:
                    cnt = copy.copy(ans[i][j - 1])
                #print("i = 1,j = 1no時ここ",cnt)
                if grid[i][j] == "+":
                    cnt[1] += 1
                else:
                    cnt[1] -= 1
                ans[i].append(cnt)

            elif ans[i][j - 1][1] > ans[i - 1][j][1]:
                cnt = copy.copy(ans[i][j - 1])
                if grid[i][j] == "+":
                    cnt[1] += 1
                else:
                    cnt[1] -= 1
                ans[i].append(cnt)

            else:
                cnt = copy.copy(ans[i - 1][j])
                if grid[i][j] == "+":
                    cnt[1] += 1
                else:
                    cnt[1] -= 1
                ans[i].append(cnt)
        
        else: # 高橋
            if ans[i][j - 1][0] == ans[i - 1][j][0]:
                if ans[i][j - 1][1] > ans[i - 1][j][1]: #上の方がいい
                    cnt = copy.copy(ans[i - 1][j])
                else:
                    cnt = copy.copy(ans[i][j - 1])
                if grid[i][j] == "+":
                    cnt[0] += 1
                else:
                    cnt[0] -= 1
                ans[i].append(cnt)

            elif ans[i][j - 1][0] > ans[i - 1][j][0]:

                cnt = copy.copy(ans[i][j - 1])
                if grid[i][j] == "+":
                    cnt[0] += 1
                else:
                    cnt[0] -= 1
                ans[i].append(cnt)

            else:
                cnt = copy.copy(ans[i - 1][j])
                if grid[i][j] == "+":
                    cnt[0] += 1
                else:
                    cnt[0] -= 1
                ans[i].append(cnt)
print(*ans,sep = "\n")
h, w = h - 1, w - 1
if ans[h][w][1] == ans[h][w][0]:
    print("Draw")
elif ans[h][w][1] > ans[h][w][0]:
    print("Aoki")
else:
    print("Takahashi")