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

def main() -> None:
    n, m = map(int, input().split())

    uf = UnionFind(n)
    ans = 0
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        if uf.same(a, b):
            ans += 1
        uf.merge(a, b)

    print(ans)

if __name__ == "__main__":
    main()