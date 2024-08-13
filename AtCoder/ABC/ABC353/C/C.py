'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc353/tasks/abc353_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc353/tasks/abc353_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right
from collections import deque

def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    q = deque()
    for i in A:
        q.append(i)
    S = [0]*(N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 0
    for i in range(N):
        p = bisect_left(A, 10**8 - A[i])
        ans += (S[N] - S[i + 1]) + A[i]*(N - i - 1)
        ans -= (N - max(p, i + 1))*(10**8)
    print(ans)

if __name__ == "__main__":
    main()