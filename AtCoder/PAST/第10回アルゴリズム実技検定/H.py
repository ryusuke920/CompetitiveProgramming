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

n, q = map(int,input().split())

uf = UnionFind(n)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        uf.merge(query[1] - 1, query[2] - 1)
    elif query[0] == 2:
        ans = []
        for i in uf.
    
ans = 0
for i in range(n):
    ans = max(ans, uf.size(i))

print(ans)