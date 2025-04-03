def calc_score(A: list, Ball: list):
    "消える個数・消えた事による点数を返す関数"
    score = 0
    for i in range(h):

        # 全て同じ石の場合
        if len(set(A[i])) == 1:
            if A[i][0] != -1:
                score += A[i] * 5
                for j in range(5):
                    Ball[j] += 1
        
        # 4つが同じ石の場合
        elif (A[i][0] == A[i][1] and A[i][1] == A[i][2] and A[i][2] == A[i][3]):
            if A[i][0] != -1:
                score += A[i][2] * 4
                for j in range(4):
                    Ball[j] += 1

        elif (A[i][1] == A[i][2] and A[i][2] == A[i][3] and A[i][3] == A[i][4]):
            if A[i][1] != -1:
                score += A[i][2] * 4
                for j in range(4):
                    Ball[j + 1] += 1

        # 3つが同じ石の場合
        elif (A[i][0] == A[i][1] and A[i][1] == A[i][2]):
            if A[i][0] != -1:
                score += A[i][2] * 3
                for j in range(3):
                    Ball[j] += 1
        elif(A[i][1] == A[i][2] and A[i][2] == A[i][3]):
            if A[i][1] != -1:
                score += A[i][2] * 3
                for j in range(3):
                    Ball[j + 1] += 1
        elif (A[i][2] == A[i][3] and A[i][3] == A[i][4]):
            if A[i][2] != -1:
                score += a[i][2] * 3
                for j in range(3):
                    Ball[j + 2] += 1
    
    return Ball, score

while True:
    h = int(input())
    if h == 0:
        exit()
    w = 5
    a = [list(map(int,input().split())) for _ in range(h)]
    
    # スコアを記録
    ans = 0

    # ボールの有無を記録する配列
    delete_ball = [[True] * 5 for _ in range(h)]
        
    # 1~5列目がそれぞれ何個消えたか
    ball = [0] * 5
    
    while True:
        cnt, num = calc_score(a, ball) # 各列の消えた個数, スコア

        # １つも消えなかった場合
        if num == 0:
            break
        else:
            for i in range(5):
                y = 0
                while True:
                    if cnt[i] <= 0:
                        break
                    if delete_ball[y][i] == True:
                        delete_ball[y][i] = False
                        cnt[i] -= 1
                    y += 1
        
        # 数字を落ちたバージョンに書き換える
        for i in range(h):
            for j in range(5):
                a[-i][j] = a[-i - cnt[j]][j]
        
        # 上の方の数字を-1に置き換える
        for i in range(h):
            for j in range(cnt[i]):
                a[i][j] = -1
    
    # 答えを出力
    print(ans)