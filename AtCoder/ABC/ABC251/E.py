import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
printd = lambda *x : print(*x, file = sys.stderr)

from math import ceil, floor, sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees
from collections import defaultdict, deque, Counter
from itertools import product, permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right

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

    # dp1[i][j] := i番目の餌をとった時、取らなかった時の最小値(1に行動を取らない)
    dp1 = [[INF] * 2 for _ in range(n + 1)]
    dp1[1][0] = 0
    for i in range(1, n):
        dp1[i + 1][1] = min(dp1[i][0], dp1[i][1]) + a[i]
        dp1[i + 1][0] = dp1[i][1]

    # dp2[i][j] := i番目の餌をとった時、取らなかった時の最小値(1に行動を取る)
    dp2 = [[INF] * 2 for _ in range(n + 1)]
    dp2[1][1] = a[0]
    for i in range(1, n):
        dp2[i + 1][1] = min(dp2[i][0], dp2[i][1]) + a[i]
        dp2[i + 1][0] = dp2[i][1]
    
    print(min(dp1[n][1], min(dp2[n])))

if __name__ == '__main__':
    main()