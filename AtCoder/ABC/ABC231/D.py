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

a = [0] * m
b = [0] * m
cnt = [0] * n
check = True

uf = UnionFind(n)

for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1

for i in range(m):
    cnt[a[i]] += 1
    cnt[b[i]] += 1
    if uf.same(a[i], b[i]) or cnt[a[i]] >= 3 or cnt[b[i]] >= 3:
        exit(print("No"))
    uf.merge(a[i], b[i])

print('Yes')