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

def RLE(S: str) -> list:
    tmp, cnt, ans = S[0], 1, []
    for i in range(1, len(S)):
        if tmp == S[i]:
            cnt += 1
        else:
            ans.append((tmp, cnt))
            tmp = S[i]
            cnt = 1

    ans.append((tmp, cnt))

    return ans


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
    S = input()
    T = input()
    s = RLE(S)
    t = RLE(T)
    #print(s)
    #print(t)
    if len(s) != len(t):
        exit(print('No'))
    
    l = len(s)
    bool = True
    for i in range(l):
        if s[i][0] != t[i][0]:
            bool = False
            break

        if s[i][1] == 1 and t[i][1] == 1:
            continue

        if s[i][1] == 1:
            bool = False
            break

        if s[i][1] > t[i][1]:
            bool = False
            break
    
    if bool:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()