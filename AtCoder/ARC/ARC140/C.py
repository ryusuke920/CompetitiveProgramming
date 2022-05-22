import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
printd = lambda *x : print(*x, file = sys.stderr)

from math import ceil, floor, sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees
from collections import defaultdict, deque, Counter
from itertools import product, permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right


def main() -> None:
    n, x = map(int, input().split())
    p = [x]
    a, b = [], []
    for i in reversed(range(1, x)):
        a.append(i)
    for i in range(x + 1, n + 1):
        b.append(i)

    ans = p + a + b
    print(*ans)

if __name__ == '__main__':
    main()