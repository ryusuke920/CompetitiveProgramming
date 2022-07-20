'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc260/tasks/abc260_a
oj t -c "python3 A.py"
oj d https://atcoder.jp/contests/abc260/tasks/abc260_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from math import sqrt, ceil, floor, sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees
from collections import defaultdict, deque, Counter
from itertools import product, permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right

def ceil(a: int, b: int) -> int:
    "calc ceil(b / a)"
    return (a + b - 1) // a

def main() -> None:
    INF = float('inf')
    mod = 1000000007
    #mod = 998244353
    s = list(input())

    if len(set(s)) == 1:
        exit(print(-1))

    if len(set(s)) == 3:
        exit(print(s[0]))

    if s[0] == s[1]:
        print(s[2])
    elif s[0] == s[2]:
        print(s[1])
    else:
        print(s[0])

    #n = int(input())
    #s = input()
    #n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    #a = [list(map(int, input().split())) for _ in range(n)]
    #s = [list(input()) for _ in range(h)]
    #grid = [list(input()) for _ in range(h)]


if __name__ == '__main__':
    main()