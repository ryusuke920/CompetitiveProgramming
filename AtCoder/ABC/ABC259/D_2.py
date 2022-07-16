import sys
input = sys.stdin.readline

def SharedPoint(x1: int, y1: int, r1: int, x2: int, y2: int, r2: int) -> int:
    """2つの円の共有点の個数を求める"""
    # (x1, y1) を中心とした半径 r1 の円
    # (x - x1) ** 2 + (y - y1) ** 2 = r1 ** 2
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    
    # r1 > r2
    if r1 < r2:
        r1, r2 = r2, r1
    
    if d == (r1 + r2) ** 2 or d == (r1 - r2) ** 2:
        return 1
    elif (r1 - r2) ** 2 < d < (r1 + r2) ** 2:
        return 2
    else:
        return 0

'''
類題
1. ABC259-D - Circumferences https://atcoder.jp/contests/abc259/tasks/abc259_d
'''


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [-1] * n


    def leader(self, a):
        while self.p[a] >= 0:
            a = self.p[a]
        return a


    def merge(self, a, b):
        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if self.p[x] > self.p[y]:
            x, y = y, x

        self.p[x] += self.p[y]
        self.p[y] = x

        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return -self.p[self.leader(a)]

n = int(input())
sx, sy, tx, ty = map(int, input().split())
x, y, r = [0] * n, [0] * n, [0] * n
for i in range(n):
    x[i], y[i], r[i] = map(int, input().split())

uf = UnionFind(n)

start, goal = [], []
for i in range(n):

    # 点は半径 0 の円として考える
    if SharedPoint(sx, sy, 0, x[i], y[i], r[i]) >= 1:
        start.append(i)
    if SharedPoint(tx, ty, 0, x[i], y[i], r[i]) >= 1:
        goal.append(i)

    for j in range(i + 1, n):
        if SharedPoint(x[i], y[i], r[i], x[j], y[j], r[j]) >= 1:
            uf.merge(i, j)

for s in start:
    for g in goal:
        if uf.same(s, g):
            exit(print('Yes'))

print('No')