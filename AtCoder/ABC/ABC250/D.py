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

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]: continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


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
    prime = primes(int(n ** (1/3)) + 1)
    print(sum([bisect_right(prime, min(n // (prime[q] ** 3), prime[q - 1])) for q in range(1, len(prime))]))

if __name__ == '__main__':
    main()