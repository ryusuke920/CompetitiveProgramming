'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc309/tasks/abc309_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc309/tasks/abc309_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

from collections import deque

def main() -> None:
    n1, n2, m = map(int, input().split())
    g = [[] for _ in range(n1 + n2)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    
    q = deque()
    d1 = [-1] * n1
    d1[0] = 0
    q.append(0)
    while q:
        v = q.popleft()
        for nxt in g[v]:
            if d1[nxt] == -1:
                q.append(nxt)
                d1[nxt] = d1[v] + 1
    
    d2 = [-1] * n2
    d2[n2 - 1] = 0
    q.append(n1 + n2 - 1)
    while q:
        v = q.popleft()
        for nxt in g[v]:
            if d2[nxt - n1] == -1:
                q.append(nxt)
                d2[nxt - n1] = d2[v - n1] + 1

    print(max(d1) + max(d2) + 1)


if __name__ == "__main__":
    main()