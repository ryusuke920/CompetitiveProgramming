'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc398/tasks/abc398_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc398/tasks/abc398_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for i in A: d[i] += 1
    ans = -1
    for i in range(N):
        if d[A[i]] == 1:
            ans = max(ans, A[i])
    if ans == -1:
        print(-1)
    else:
        for i in range(N):
            if A[i] == ans:
                exit(print(i + 1))


if __name__ == "__main__":
    main()