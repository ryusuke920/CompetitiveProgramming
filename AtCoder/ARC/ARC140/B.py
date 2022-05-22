import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
printd = lambda *x : print(*x, file = sys.stderr)

from math import ceil, floor, sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees
from collections import defaultdict, deque, Counter
from itertools import product, permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right


def min_int(a: int, b: int) -> int:
    "2数の最小値"
    return a if a <= b else b


def min_lit(a: list) -> int:
    "リストの最小値"
    global INF
    cnt = INF
    for i in range(len(a)):
        if a[i] < cnt:
            cnt = a[i]

    return cnt


def min_lit(a: list) -> int:
    "リストの最大値"
    global INF
    cnt = -INF
    for i in range(len(a)):
        if a[i] > cnt:
            cnt = a[i]

    return cnt


def max_int(a: int, b: int) -> int:
    "2数の最大値"
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
    n = int(input())
    s = input()

    if n <= 2:
        exit(print(0))

    num, arc = [], [0] * 3
    for i in s:
        if i == 'A':
            if arc[2] > 0:
                num.append(min(arc[0], arc[2]))
                arc = [1, 0, 0]
            elif arc[1] > 0:
                arc = [1, 0, 0]
            else:
                arc[0] += 1
        elif i == 'R':
            if arc[2] > 0:
                num.append(min(arc[0], arc[2]))
                arc = [0] * 3
            elif arc[0] == 0 or arc[1] > 0:
                arc = [0] * 3
            else:
                arc[1] = 1
        elif i == 'C':
            if arc[1] == 1:
                arc[2] += 1
            else:
                arc = [0] * 3
    
    if arc[2] >= 1:
        num.append(min(arc[0], arc[2]))

    if len(num) == 0:
        exit(print(0))

    num.sort()
    cnt = 0
    q = deque()
    for i in num:
        if i == 1:
            cnt += 1
        else:
            q.append(i)

    ans = 0
    while q:
        v = q.popleft()
        if cnt >= v - 1:
            cnt -= v - 2
            ans += 2 * (v - 1)
        else:
            ans += cnt * 2
            v -= cnt
            q.appendleft(v)
            cnt = 0
            break

    ans += cnt if cnt >= 1 else len(q) * 2

    print(ans)

if __name__ == '__main__':
    main()