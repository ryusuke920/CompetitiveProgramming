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
    dp = [0] * (n + 1)
    for i in range(n):
        cnt = 0
        for j in reversed(range(i + 2)):
            dp[j] = dp[j - 1] + d[j] + x[i]
            cnt = max(cnt, dp[j - 1])
        dp[0] = cnt
    
    print(max(dp))


if __name__ == "__main__":
    main()