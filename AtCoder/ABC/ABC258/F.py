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

    #n = int(input())
    #s = input()
    n, q, x = map(int, input().split())
    w = list(map(int, input().split()))
    #a = [list(map(int, input().split())) for _ in range(n)]
    #s=[list(input()) for _ in range(h)]
    
    weight = 0
    for i in range(n):
        weight += w[i]
        if weight >= x:
            cnt = i + 1
            break
    
    now_l, nxt_l = [], []
    if weight >= x:
        now_l.append(cnt)
        nxt_l.append((i + 1) % n)
    else:
        p = x // weight
        weight *= p
        cnt *= p
        for i in range(n):
            weight += w[i]
            cnt += 1
            if weight >= x:
                break
        now_l.append(cnt)
        ind = (i + 1) % n
        nxt_l.append(ind)
    
    for i in range(1, n):
        weight -= w[i - 1]
        cnt -= 1

        while True:
            if weight >= x:
                break
            weight += w[ind]
            cnt += 1
            ind += 1
            ind %= n
        
        now_l.append(cnt)
        nxt_l.append(ind)
    
    



    


if __name__ == '__main__':
    main()