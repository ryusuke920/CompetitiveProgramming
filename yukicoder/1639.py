# クラスカル法

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
    if self.p[x] > self.p[y]:
      x, y = y, x
    self.p[x] += self.p[y]
    self.p[y] = x
    return x

  def same(self, a, b): return self.leader(a) == self.leader(b)

  def size(self, a): return -self.p[self.leader(a)]

n = int(input())
uf = UnionFind(n)
# (a, b, cost)の無向グラフ
g = [list(map(int, input().split())) for _ in range(n * (n - 1) // 2)]
g.sort(key=lambda x: x[2])

ans = 0
for i, j, cost in g:
    if uf.same(i - 1, j - 1): continue
    uf.merge(i - 1, j - 1)
    ans = max(ans, cost)

print(ans)