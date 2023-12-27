'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc327/tasks/abc327_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc327/tasks/abc327_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(500_000)

def dfs(now: int) -> None:
    for to in g[now]:
        if s[to] == -1:
            s[to] = 1 - s[now]
            dfs(to)
        elif s[to] == s[now]:
            exit(print("No"))

def main():
    global n, m, a, b, g, s
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = [i - 1 for i in a]
    b = [i - 1 for i in b]

    g = [[] for _ in range(n)]
    for i in range(m):
        g[a[i]].append(b[i])
        g[b[i]].append(a[i])

    s = [-1] * n
    for i in range(n):
        if s[i] == -1:
            s[i] = 0
            #print(s)
            dfs(i)

    print("Yes")


if __name__ == "__main__":
    main()
