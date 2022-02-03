K = int(input()) # 9k枚
s = list(input())
t = list(input())
cnt = [0] * 9
for i in range(4):
    cnt[int(s[i]) - 1] += 1
    cnt[int(t[i]) - 1] += 1

under = (9 * K - 8) * (9 * K - 9)
up = 0
for i in range(9): # 高橋君の札
    for j in range(9): # 青木君の札
        takahashi_point = aoki_point = 0
        taka_num = [0] * 9 # 高橋君の札の枚数
        aoki_num = [0] * 9 # 青木君の札の枚数
        if i == j:
            if cnt[i] + 2 >= K + 1: continue # k枚以上ある時はスキップ

            # 青木君と高橋君の持ってる枚数をカウント
            for k in range(4):
                taka_num[int(s[k]) - 1] += 1 # 0index
                aoki_num[int(t[k]) - 1] += 1 # 0index
            taka_num[i] += 1
            aoki_num[j] += 1

            # 青木君と高橋君の点数を集計
            for k in range(9):
                takahashi_point += (k + 1) * (10 ** taka_num[k])
                aoki_point += (k + 1) * (10 ** aoki_num[k])
            
            # 合計点数で比較
            if takahashi_point > aoki_point:
                up += (K - cnt[i]) * (K - cnt[i] - 1)

        elif i != j:
            if cnt[i] + 1 >= K + 1 or cnt[j] + 1 >= K + 1: continue

            # 青木君と高橋君の持ってる枚数をカウント
            for k in range(4):
                taka_num[int(s[k]) - 1] += 1 # 0index
                aoki_num[int(t[k]) - 1] += 1 # 0index
            taka_num[i] += 1
            aoki_num[j] += 1

            # 青木君と高橋君の点数を集計
            for k in range(9):
                takahashi_point += (k + 1) * (10 ** taka_num[k])
                aoki_point += (k + 1) * (10 ** aoki_num[k])

            # 合計点数で比較
            if takahashi_point > aoki_point:
                up += (K - cnt[i]) * (K - cnt[j])

print(up / under)