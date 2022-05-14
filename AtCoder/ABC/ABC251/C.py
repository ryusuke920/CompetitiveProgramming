import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
printd = lambda *x : print(*x, file = sys.stderr)

from math import ceil, floor, sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees
from collections import defaultdict, deque, Counter
from itertools import product, permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right


def min(a: int, b: int) -> int:
    "最小値"
    return a if a <= b else b


def max(a: int, b: int) -> int:
    "最大値"
    return a if a >= b else b


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
    n = int(input())
    d = defaultdict(lambda: -1)
    ans = []
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if d[s] == -1:
            d[s] = t
            ans.append((t, i + 1))
    ans.sort(reverse=True, key=lambda x: x[0])
    print(ans[0][1])


if __name__ == '__main__':
    main()