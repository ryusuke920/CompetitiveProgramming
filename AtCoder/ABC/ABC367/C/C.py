'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc367/tasks/abc367_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc367/tasks/abc367_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
sys.setrecursionlimit(500_000)

def dfs(i, j, cnt, l):
    if j == N:
        if cnt % K == 0:
            print(" ".join(map(str, l)))
        return
    
    for k in range(1, R[j] + 1):
        l.append(k)
        dfs(k, j + 1, cnt + k, l)
        l.pop()


N, K = map(int, input().split())
R = list(map(int, input().split()))
dfs(0, 0, 0, [])
from itertools import permutations
# for i in permutations(range(N)):