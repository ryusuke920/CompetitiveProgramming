import sys
input = sys.stdin.readline

from math import ceil, floor, sin, cos, tan, acos, asin, atan, radians, factorial, exp, degrees
from collections import defaultdict, deque, Counter
from itertools import product, permutations, combinations, combinations_with_replacement
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right


def min_int(a: int, b: int) -> int:
    "2数の最小値"
    return a if a <= b else b


def min_list(a: list) -> int:
    "リストの最小値"
    global INF
    cnt = INF
    for i in range(len(a)):
        if a[i] < cnt:
            cnt = a[i]

    return cnt


def min_list(a: list) -> int:
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


def solve(weight: int, t: int) -> tuple:

    ans, p = [], -10 ** 4
    const = 10 ** 4

    num = const // (t // 2)

    for i in range(-(t // 2) + 1, t // 2):
        ans.append((num * i, 0, num * i, 1))

    sb = [0] * t
    m = set([num * i for i in range(-(t // 2) + 1, t // 2)])

    for x, y in xy:

        if x in m:
            continue

        if y != p and sb != [0] * t:
            check = 0
            for i in sb:
                if i < 10:
                    continue
                for i in sb:
                    if i == 0 or i > 10:
                        continue
                    a[i - 1] -= 1
                ans.append((-const, p, const, p))
                sb = [0] * t
                check = 1
                break

            if check == 0:
                cnt = 0
                for i in sb:
                    if i != 0:
                        if a[i - 1] > 0:
                           cnt += i

                if cnt > weight:
                    for i in sb:
                        a[i - 1] -= 1
                    ans.append((-const, p + 1, const, p + 1))
                    sb = [0] * t

            if len(ans) >= 100:
                    break

        for i in range(-(t // 2) + 1, t // 2 + 1):
            if x < num * i:
                sb[i + (t // 2) - 1] += 1
                break

        p = y

    point = n
    for i in a:
        if i > 0:
            point -= i
    
    return ans, point

n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]
xy.sort(key=lambda x: x[1])

def main() -> None:
    INF = float('inf')
    k = 5
    ans, point = solve(k, k * 2)
    for i in range(10):
        cnt, cnt_score = solve(k, k * 2 + 2 + i * 2)
        if cnt_score > point:
            ans = cnt

    print(len(ans))
    for px ,py, qx, qy in ans:
        print(px, py, qx, qy)

if __name__ == '__main__':
    main()