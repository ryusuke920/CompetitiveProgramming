'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc337/tasks/abc337_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc337/tasks/abc337_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(500_000)

def dfs(now: int, prev :int) -> None:
    ans.append(now + 1)
    for nxt in g[now]:
        if nxt == prev:
            continue
        dfs(nxt, now)


ans = []
n = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))

g = [[] for _ in range(n)]
for i in range(n):
    if a[i] >= 0:
        g[a[i]].append(i)
        g[i].append(a[i])
    else:
        start = i

dfs(start, -1)

print(*ans)