"""
https://betrue12.hateblo.jp/entry/2019/08/22/001522
この記事が天才すぎました、ありがとうございます！！！
"""

s = list(input())
# dp[i][j] := i文字目まで見た時の13で割ったあまりがjであるものの個数
l = len(s)
dp = [[0] * 13 for _ in range(l + 1)]
dp[0][0] = 1
mod = 10 ** 9 + 7
for i in range(len(s)):
    if s[i] == "?":
        for j in range(13):
            for k in range(10):
                """
                dp[i][j]の時点ではあまりがjのやつ
                これに１個数字を引っ付ける（x）と、あまりは10*j+xになる
                だからt = 10*j+xとして、dp[i+1][10*j+x]にdp[i][j]を足す
                jは0~12まで、xは0~9まであるのでそれをfor文で回す
                """
                dp[i + 1][(j * 10 + k) % 13] += dp[i][j] # あまりを10倍して、数字を１つ足すイメージ
                dp[i + 1][(j * 10 + k) % 13] %= mod
    else:
        for j in range(13):
            dp[i + 1][(j * 10 + int(s[i])) % 13] = dp[i][j]
            dp[i + 1][(j * 10 + int(s[i])) % 13] %= mod

print(dp[l][5] % mod)