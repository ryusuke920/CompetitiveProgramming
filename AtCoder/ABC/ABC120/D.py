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

n, m = map(int,input().split())
ab = [list(map(int, input().split())) for _ in range(m)][::-1]

uf = UnionFind(n)

ans = [n * (n - 1) // 2]
for i in range(m - 1):
    a, b = ab[i]
    if uf.same(a - 1, b - 1):
        ans.append(ans[-1])
    else:
        ans.append(ans[-1] - uf.size(a - 1) * uf.size(b - 1))
    uf.merge(a - 1, b - 1)

print(*ans[::-1], sep='\n')