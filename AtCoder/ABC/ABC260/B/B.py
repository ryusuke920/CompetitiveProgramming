'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc260/tasks/abc260_b
oj t -c "python3 a.py"
oj d https://atcoder.jp/contests/abc260/tasks/abc260_b b.py --guess-python-interpreter pypy

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
    INF = float('inf')
    mod = 1000000007
    #mod = 998244353
    
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i], b[i], a[i] + b[i], i))

    is_ok = set()

    c.sort(key=lambda x: (-x[0], x[3]))

    for i in range(n):
        if len(is_ok) == x:
            break
        is_ok.add(c[i][3])
        
    c.sort(key=lambda x:(-x[1], x[3]))

    for i in range(n):
        if len(is_ok) == x + y:
            break

        if c[i][3] in is_ok:
            continue
        is_ok.add(c[i][3])
        

    c.sort(key=lambda x: (-x[2], x[3]))

    for i in range(n):
        if len(is_ok) == x + y + z:
            break
        if c[i][3] in is_ok:
            continue
        is_ok.add(c[i][3])

    for i in sorted(list(is_ok)):
        print(i + 1)


    #n = int(input())
    #s = input()
    #n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    #a = [list(map(int, input().split())) for _ in range(n)]
    #s = [list(input()) for _ in range(h)]
    #grid = [list(input()) for _ in range(h)]


if __name__ == '__main__':
    main()