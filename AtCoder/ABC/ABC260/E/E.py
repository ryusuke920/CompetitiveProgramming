'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc260/tasks/abc260_e
oj t -c "python3 A.py"
oj d https://atcoder.jp/contests/abc260/tasks/abc260_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(500_000)
printd = lambda *x : print(*x, file = sys.stderr)
 
from math import sqrt, ceil, floor, sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees
from collections import defaultdict, deque, Counter
from itertools import product, permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right

def ceil(a: int, b: int) -> int:
    "calc ceil(b / a)"
    return (a + b - 1) // a

def main() -> None:
    n, m = map(int, input().split())

    p = [[] for _ in range(m + 1)]
    
    r, min_b = 0, m
    for _ in range(n):
        a, b = map(int, input().split())
        p[a].append(b)
        r = max(r, a)
        min_b = min(min_b, b)

    ans = [0] * (m + 2)
    for l in range(1, min_b + 1):
        ans[r - l + 1] += 1
        if m - l + 1 + 1 <= m:
            ans[m - l + 1 + 1] -= 1
        if p[l] == []:
            continue
        r = max(r, max(p[l]))
    
    for i in range(m):
        ans[i + 1] += ans[i]

    print(*ans[1:m + 1])


if __name__ == '__main__':
    main()