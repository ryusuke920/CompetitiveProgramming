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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = defaultdict(set)
    s[1].add(a[0])
    t = defaultdict(set)
    t[1].add(b[0])
    for i in range(2, n + 1):
        s[i] |= s[i - 1]
        s[i].add(a[i - 1])
        t[i] |= t[i - 1]
        t[i].add(b[i - 1])

    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        print('Yes') if s[x] == t[y] else print('No')


if __name__ == '__main__':
    main()