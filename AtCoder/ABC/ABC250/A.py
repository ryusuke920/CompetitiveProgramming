import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
printd = lambda *x : print(*x, file = sys.stderr)

from math import ceil, floor, sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees
from collections import defaultdict, deque, Counter
from itertools import product, permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right
def divisors(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)

    divisor.sort()
    return divisor

def min(a: int, b: int) -> int:
    "最小値"
    return a if a <= b else b


def max(a: int, b: int) -> int:
    "最大値"
    return a if a >= b else b


def OutOfRange(h: int, w: int, vy: int, vx: int) -> int:
    "BFSなどの配列外参照"
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    cnt = 0
    for dy, dx in d:
        y = vy + dy
        x = vx + dx
        if not (0 <= x < w and 0 <= y < h):
            cnt += 0
        else:
            cnt += 1

    return cnt


def main() -> None:
    h, w = map(int, input().split())
    r, c = map(lambda x: int(x) - 1, input().split())
    print(OutOfRange(h, w, r, c))


if __name__ == '__main__':
    main()