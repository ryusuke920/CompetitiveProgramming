# dp[i][j] := i番目までみた時の７で割り切れる数がjの個数
n = int(input())
from random import randint
def solve(num: int):
    s = []
    for _ in range(num):
        s.append(randint(0, 9))
    s = s[::-1]
    s = [0] + s # 累積和を取るので便宜上 0 を先頭につける
    mod = 7
    for i in range(len(s) - 1):
        s[i + 1] *= pow(10, i, mod)
        s[i + 1] %= mod

    # 累積和を取る
    for i in range(len(s) - 2):
        s[i + 2] += s[i + 1]
        s[i + 2] %= mod

    #print(s)
    # [l, r] のとき、 S_{l-1} ≡ S_{r} が成り立てば良い
    cnt = [0] * mod
    for i in range(len(s)):
        cnt[s[i]] += 1

    ans = 0
    for i in range(mod):
        ans += cnt[i] * (cnt[i] - 1) // 2
    
    return ans, s

num = 100
while True:
    ans, s = solve(num)
    s = list(map(str, s))
    t = int("".join(s)[1:][::-1])

    if ans == n:
        exit(print(t))
    elif ans < n:
        num *= 2
        num = int(num)
    else:
        num *= 0.8
        num = int(num)
        num = max(num, 1)
    
    #print(ans,s)