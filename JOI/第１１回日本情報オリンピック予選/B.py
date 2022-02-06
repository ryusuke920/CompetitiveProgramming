n = int(input())
game = n * (n - 1) // 2
score = [[0, 0, 0] for _ in range(n)] # チーム番号、点数、順位 
for i in range(n):
    score[i][0] = i + 1

for i in range(game):
    x, y, a, b = map(int,input().split())
    if a == b:
        score[x - 1][1] += 1
        score[y - 1][1] += 1
    elif a > b:
        score[x - 1][1] += 3
    else:
        score[y - 1][1] += 3

rank = 1 # 順位
score.sort(key = lambda x: x[1]) # スコア順にソート(昇順)
score = score[::-1]
score[0][2] = rank
cnt = 0 # 順位貯め
# print(score, "スコア順") # スコア順
for i in range(n - 1):
    if score[i][1] != score[i + 1][1]:
        rank += 1 + cnt
        score[i + 1][2] = rank
        cnt = 0
    else:
        score[i + 1][2] = rank
        cnt += 1 

score.sort(key = lambda x: x[0]) # チーム番号順にソート
#print(score, "チーム番号順")
for i in range(n):
    print(score[i][2])