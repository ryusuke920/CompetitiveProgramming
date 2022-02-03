import sys
input = sys.stdin.readline
n, m, q = map(int,input().split()) # 荷物、はこ、クエリ
w, v = [0] * n, [0] * n # 大きさ、価値

for i in range(n):
    w[i], v[i] = map(int,input().split())

x = list(map(int,input().split()))

for i in range(q):
    box = [[True, 0] for _ in range(m)] # 荷物が入るかの有無・入る量
    l, r = map(int,input().split())

    # 箱に入れられるかの判定
    for j in range(l, r + 1):
        box[j - 1][0] = False
    
    # 荷物の入れられる最大値の判定
    for j in range(m):
        box[j][1] = x[j]
    box.sort(key = lambda x: x[1])

    nimotu = [[0, 0, True] for _ in range(n)] # 荷物の大きさ、価値、詰めたかどうかの有無
    for j in range(n):
        nimotu[j][0], nimotu[j][1] = w[j], v[j]
    
    # 価値の大きい順にソート
    nimotu.sort(key = lambda x: x[1], reverse = True)

    ans = 0
    for j in range(m):
        if box[j][0] == False: continue # 使えない箱だったらスルー
        for k in range(n): # 入れれる箱の場合どの荷物を詰めるかを見ていく
            if nimotu[k][2] == True and box[j][1] >= nimotu[k][0]:
                nimotu[k][2] = False
                ans += nimotu[k][1]
                break
    print(ans)