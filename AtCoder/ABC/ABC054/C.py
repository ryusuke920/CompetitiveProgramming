import itertools
n,m = map(int,input().split())
x = [[0]*n for _ in range(n)]

# 入力された辺をつなげる
for i in range(m):
    a,b = map(int,input().split())
    x[a-1][b-1] = 1
    x[b-1][a-1] = 1

ans = 0 # 答えとなる場合の数
for i in itertools.permutations(range(n)):
    if i[0] != 0:
        break
    ch = 1 # それぞれのパターンでゴールまで辿れられたら１のままになる（不適の場合は０）
    for j in range(n-1):
        ch *= x[i[j]][i[j+1]] #ここ意外とミスりやすい
    if ch == 1: # かけて１なら解を追加
        ans += 1
print(ans)