n, k = map(int, input().split())
a = list(map(int, input().split()))

# dp[i] := 石が残り i 個の際に先手が勝つかどうか
dp = [False] * (k + 1)
# dp[0] = False
# 負ける手番を見つけれれば自分がそれに持っていけば必ず負かせれるので勝てる（=True）
for i in range(k + 1):
    for j in range(n):
        # 石が i 個時に a_i を選ぶことを考える
        if i - a[j] >= 0:
            if dp[i - a[j]] == False:
                dp[i] = True

if dp[k]:
    print("First")
else:
    print("Second")