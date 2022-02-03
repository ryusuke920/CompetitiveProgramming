n = int(input())
a = list(map(int,input().split()))
ans = 0 # 累積和
cnt_1 = cnt_2 = 0 # 試行した回数

# +, -, + , ...のパターン
for i in range(n):
    if i % 2 == 0: # +の時
        ans += a[i]
        if ans <= 0:
            cnt_1 += abs(ans) + 1
            ans = 1
    else: # i % 2 == 1 # -の時
        ans += a[i]
        if ans >= 0:
            cnt_1 += ans + 1
            ans = -1

ans = 0 # 再び初期化
# -, +, - , ...のパターン
for i in range(n):
    if i % 2 == 0: # -の時
        ans += a[i]
        if ans >= 0:
            cnt_2 += ans + 1
            ans = -1
    else: # i % 2 == 1 # +の時
        ans += a[i]
        if ans <= 0:
            cnt_2 += abs(ans) + 1
            ans = 1

print(min(cnt_1,cnt_2))