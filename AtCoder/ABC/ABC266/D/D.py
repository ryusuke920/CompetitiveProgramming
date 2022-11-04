'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc268/tasks/abc268_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc268/tasks/abc268_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    
    # dp[i][j] := 時刻 i に座標 j にいるときの合計の最大値
    max_t = p[-1][0]
    dp = [[0] * 5 for _ in range(max_t + 1)]

    snuke = [[0] * 5 for _ in range(max_t + 1)]
    for i in range(n):
        t, x, a = p[i]
        if t <= 3 and t < x:
            continue
        snuke[t][x] = a

    for i in range(1, max_t + 1):
        for j in range(5):
            if j == 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j + 1], dp[i - 1][j]) + snuke[i][j]
            elif j == 4:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1], dp[i - 1][j]) + snuke[i][j]
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j + 1], dp[i - 1][j - 1], dp[i - 1][j]) + snuke[i][j]
        

    print(max(dp[max_t]))


if __name__ == "__main__":
    main()