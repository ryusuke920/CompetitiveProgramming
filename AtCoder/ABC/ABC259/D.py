import sys
input = sys.stdin.readline

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
uf = UnionFind(n)
sx, sy, tx, ty=  map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        r1 = l[i][2]
        r2 = l[j][2]

        if r1 < r2:
            r1, r2 = r2, r1
        xi, yi, xj, yj = l[i][0], l[i][1], l[j][0], l[j][1]
        d = (xi - xj) ** 2 + (yi - yj) ** 2

        if (r1 - r2) ** 2 <= d and d <= (r1 + r2) ** 2:
            uf.merge(i, j)

start = []
goal = []
for i in range(n):
    x, y, r = l[i]
    if (x - sx) ** 2 + (y - sy) ** 2 == r ** 2:
        start.append(i)
    if (x - tx) ** 2 + (y - ty) ** 2 == r ** 2:
        goal.append(i)
    
bool = False
for i in start:
    for j in goal:
        if uf.same(i, j):
            bool = True
            break

if bool:
    print('Yes')
else:
    print('No')