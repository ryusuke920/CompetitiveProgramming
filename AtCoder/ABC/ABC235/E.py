# クラスカル法
# 出典：https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f

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

n, m, q = map(int, input().split())
uf = UnionFind(n)
g = []
for _ in range(m):
    a, b, c = map(int, input().split())
    g.append((a - 1, b - 1, c, -1))

for i in range(q):
    u, v, w = map(int, input().split())
    g.append((u - 1, v - 1, w, i))

# 第4引数が -1 -> 常に存在するノード, 0以上 -> その場限りのノード
g.sort(key=lambda x: x[2])
ans = [None] * q
for i in range(m + q):
    if g[i][3] == -1:
        if uf.same(g[i][0], g[i][1]): continue
        uf.merge(g[i][0], g[i][1])
    elif g[i][3] >= 0:
        if uf.same(g[i][0], g[i][1]):
            ans[g[i][3]] = 'No'
        else:
            ans[g[i][3]] = 'Yes'

for i in range(q):
    print(ans[i])