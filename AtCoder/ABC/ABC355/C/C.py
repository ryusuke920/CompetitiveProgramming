'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc355/tasks/abc355_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc355/tasks/abc355_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N, T = map(int, input().split())
    A = list(map(lambda x: int(x) - 1, input().split()))
    h = [0]*N
    w = [0]*N
    l = [0, 0]
    for i in range(T):
        y, x = A[i] // N, A[i] % N
        h[y] += 1
        w[x] += 1
        if y == x:
            l[0] += 1
        if y + x == N - 1:
            l[1] += 1
        if h[y] == N or w[x] == N or l[0] == N or l[1] == N:
            exit(print(i + 1))

    print(-1)


if __name__ == "__main__":
    main()