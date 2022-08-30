'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc261/tasks/abc261_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc261/tasks/abc261_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from collections import defaultdict
def main() -> None:
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(m):
        c, y = map(int, input().split())
        d[c] = y
    # dp[i][j] := i 番目の操作で j を出した時の最大値
    # j = 0:ura, j = 1, omote
    dp = [[-1] * 2 for _ in range(n + 1)]
    for j in range(2):
            dp[0][j] = 0
    
    num = [-1] * n

    for i in range(n):
        for j in range(2):
            if j == 0:
                dp[i + 1][0] = max(dp[i])
            elif j == 1:
                dp[i + 1][1] = max(dp[i][1] + d[])
        print(*dp, sep='\n')
        print()
    print(max(max(dp[n][1]), max(dp[n][0])))

if __name__ == "__main__":
    main()