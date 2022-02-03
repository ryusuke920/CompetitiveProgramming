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

n, m, k = map(int,input().split())

uf = UnionFind(n)

out = [[] for _ in range(n)] # 友達もしくは同じグループの中で喧嘩の組み合わせの集合
for _ in range(m):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    uf.merge(a, b)
    out[a].append(b)
    out[b].append(a)

for _ in range(k):
    c, d = map(int,input().split())
    c -= 1
    d -= 1
    if uf.same(c, d):
        out[c].append(d)
        out[d].append(c)

ans = []
for i in range(n):
    ans.append(uf.size(i) - len(out[i]) - 1)

print(*ans)