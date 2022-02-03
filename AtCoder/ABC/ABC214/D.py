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
    if x == y: return x
    if self.p[x] > self.p[y]: x, y = y, x
    self.p[x] += self.p[y]
    self.p[y] = x
    return x

  def same(self, a, b): return self.leader(a) == self.leader(b)

  def size(self, a): return -self.p[self.leader(a)]

n = int(input())
uf = UnionFind(n)

e = []
for _ in range(n - 1):
    u, v, w = map(int,input().split())
    e.append((w, u - 1, v - 1))
e.sort()

ans = 0
for i in range(n - 1):
    ans += e[i][0] * uf.size(e[i][1]) * uf.size(e[i][2])
    uf.merge(e[i][1], e[i][2])

print(ans)