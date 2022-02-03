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
ab.sort(reverse=True, key=lambda x: (x[0], x[1]))

cnt = []
ans = 0
now = 0
for i in range(n):
    ans += 1
    while True:
        if now < m:
            if ab[now][0] >= n - i:
                if uf.same(ab[now][0] - 1, ab[now][1] - 1):
                    now += 1
                else:
                    ans -= 1
                    uf.merge(ab[now][0] - 1, ab[now][1] - 1)
                    now += 1
            else:
                break
        else:
            break
    cnt.append(ans)


print(*cnt[:-1][::-1], sep="\n")
print(0)