import sys
input = sys.stdin.readline
n, k = map(int,input().split())

check = [0] * n # 0 := i日目のおやつが決まっていない
# 入力
for i in range(k):
    # b = (1 := トマトソース, 2 := クリームソース, 3 := バジルソース)
    a, b = map(int,input().split())
    check[a - 1] = b # 0index
print(check)
# 3 ^ (n - k) 文の組み合わせがある

dp = [[[0] * 4 for _ in range(4)] for _ in range(n + 1)]
dp[0][0][0] = 1

mod = 10 ** 4
for i in range(n): # 日にち
    for j in range(4): # 2日前のおやつ
        for k in range(4): # 1日前のおやつ
            for l in range(1, 4): # 今日のおやつ
                # i日目が決まっていて、違うおやつの場合
                if check[i] != 0 and check[i] != l: continue
                # 3日連続で同じおやつの時
                if j == k and k == l: continue
                dp[i + 1][l][k] += dp[i][k][j] % mod
#print(*dp,sep = "\n")

ans = 0 # 出力
for i in range(4):
    for j in range(4):
        ans += dp[-1][i][j] % mod
print(ans % mod)