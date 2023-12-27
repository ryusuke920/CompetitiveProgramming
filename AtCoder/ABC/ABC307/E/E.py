'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc307/tasks/abc307_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc307/tasks/abc307_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, m = map(int, input().split())
    mod = 998244353

    #ans = m * pow(m - 1, n - 2, mod) * (m - 2)
    #print(ans % mod)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = m

    for i in range(1, n - 1):
        dp[i][0] = dp[i - 1][0] * (m - 2) + dp[i - 1][1] * (m - 1)
        dp[i][0] %= mod

        dp[i][1] = dp[i - 1][0]
        dp[i][1] %= mod
    
    ans = dp[n - 2][1] * (m - 1) + dp[n - 2][0] * (m - 2)
    ans %= mod

    print(ans)


if __name__ == "__main__":
    main()