'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc306/tasks/abc306_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc306/tasks/abc306_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    x, y = [0] * n, [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    
    # dp[i][j] := i 番目までの料理を見て、状態が j の時の最大値
    dp = [[-1] * 4 for _ in range(n + 1)]
    for i in range(4):
        dp[0][i] = 0
    for i in range(n):
        if x[i] == 0:
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][0] + y[i], dp[i][1] + y[i])
        if x[i] == 1:
            dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + y[i])
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][0])
        dp[i + 1][1] = max(dp[i + 1][1], dp[i][1])
    
    #print(*dp, sep="\n")
    print(max(dp[n]))

if __name__ == "__main__":
    main()