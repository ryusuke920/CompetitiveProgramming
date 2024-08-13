'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc350/tasks/abc350_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc350/tasks/abc350_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

def dfs(n):
    if n == 0:
        return 0

    if d[n] != -INF:
        return d[n]

    num = INF
    p = Y * 6 / 5
    num = min(num, dfs(n // A) + X)
    for i in range(2, 7):
        p += dfs(n // i) / 5
    num = min(num, p)
    # num = min(num, dfs(n // A) + X, p)
    d[n] = num

    return num

N, A, X, Y = map(float, input().strip().split())
INF = 10**18
d = defaultdict(lambda: -INF)
print(dfs(N))