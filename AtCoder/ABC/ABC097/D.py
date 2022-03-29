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

n, m = map(int, input().split())
p = list(map(int, input().split()))

uf = UnionFind(n)
xy = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

for i in range(m):
    u, v = xy[i]
    uf.merge(u, v)

g = [set() for _ in range(n)]
for i in range(m):
    u, v = xy[i]
    g[uf.leader(u)].add(u + 1)
    g[uf.leader(v)].add(v + 1)

ans = 0
for i in range(n):
    if p[i] in g[uf.leader(i)]:
        ans += 1
    if len(g[uf.leader(i)]) == 0 and p[i] - 1 == i:
        ans += 1

print(ans)