import sys
input = sys.stdin.readline
sys.setrecursionlimit(500_000)
printd = lambda *x : print(*x, file = sys.stderr)

from math import ceil, floor, sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees
from collections import defaultdict, deque, Counter
from itertools import product, permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right


def min_int(a: int, b: int) -> int:
    "2数の最小値"
    return a if a <= b else b


def max_int(a: int, b: int) -> int:
    "2数の最大値"
    return a if a >= b else b


def min_list(a: list) -> int:
    "リストの最小値"
    global INF
    cnt = INF
    for i in range(len(a)):
        if a[i] < cnt:
            cnt = a[i]

    return cnt


def max_list(a: list) -> int:
    "リストの最大値"
    global INF
    cnt = -INF
    for i in range(len(a)):
        if a[i] > cnt:
            cnt = a[i]

    return cnt


def OutOfRange(h: int, w: int, vy: int, vx: int) -> bool:
    "BFSなどの配列外参照"
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for dy, dx in d:
        y = vy + dy
        x = vx + dx
        if not (0 <= x < w and 0 <= y < h):
            return False
        else:
            return True


def main() -> None:
    INF = 10 ** 18
    mod = 10 ** 9 + 7
    #mod = 998244353

    n = int(input())
    #s = input()
    #n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    #s=[list(input()) for _ in range(h)]
    t = 2 * 10 ** 5 + 2
    s = [0] * t
    for i in range(n):
        x, y = a[i]
        s[x] += 1
        s[y] -= 1
    
    for i in range(len(s) - 1):
        s[i + 1] += s[i]
    
    check = False
    for i, j in enumerate(s):
        if not check:
            if j != 0:
                check = True
                start = i
        else:
            if j != 0:
                continue
            else:
                print(start, i)
                check = False
    

    


if __name__ == '__main__':
    main()