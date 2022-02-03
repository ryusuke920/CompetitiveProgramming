from sys import setrecursionlimit
setrecursionlimit(10 ** 7)
import sys
input = sys.stdin.readline

h, w, D = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
from collections import defaultdict
d = defaultdict(int)
for i in range(h):
    for j in range(w):
        a[i][j] -= 1
        d[a[i][j]] = (i, j)

memo = [0] * (h * w)
def f(x: int) -> int:
    if memo[x] != 0: return memo[x]
    if x < D: return 0
    y = x - D
    cost = abs(d[x][0] - d[y][0]) + abs(d[x][1] - d[y][1])
    cnt = cost + f(y)
    memo[x] = cnt
    return memo[x]

q = int(input())
for _ in range(q):
    l, r = map(int,input().split())
    l -= 1
    r -= 1
    print(f(r) - f(l))