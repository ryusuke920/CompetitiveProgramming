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

uf = UnionFind(n)

ab = [list(map(int,input().split())) for _ in range(m)]
for i in range(m):
    uf.merge(ab[i][0] - 1, ab[i][1] - 1)

par = [-1] * n
for i in range(n):
    par[i] = uf.leader(i)

cnt = [0] * n
for i in par:
    cnt[i] += 1

edge = [0] * n
for i in range(m):
    t = ab[i][0] - 1
    num = par[t]
    edge[num] += 1

mod = 998244353
ans = 0
for i, j in zip(cnt, edge):
    if i != j:
        exit(print(0))

    if i == j and i >= 3:
        ans += 1

if ans:
    print(pow(2, ans, mod))
else:
    print(0)