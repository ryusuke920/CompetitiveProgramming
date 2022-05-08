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
    n, q = map(int, input().split())
    ans = defaultdict(int) # ans[i] := 左から i 番目に入っているボールの数字
    num = defaultdict(int) # num[i] := i が今何番目にいるか
    for i in range(n):
        ans[i + 1] = i + 1
        num[i + 1] = i + 1
    
    for _ in range(q):
        x = int(input()) # 入れ替えたい数
        now_x = num[x] # xのある場所
        if now_x != n:
            y = ans[now_x + 1] # x のある場所の隣にある数
            now_y = num[y] # y のある場所
        else:
            y = ans[now_x - 1] # x のある場所の隣にある数
            now_y = num[y] # y のある場所
        ans[now_x], ans[now_y] = ans[now_y], ans[now_x] # 2つの数を入れ替える
        num[x], num[y] = num[y], num[x] # 2つのある場所を入れ替える
    
    t = []
    for i in range(n):
        t.append(ans[i + 1])
    print(*t)

if __name__ == '__main__':
    main()