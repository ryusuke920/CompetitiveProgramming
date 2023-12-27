from itertools import permutations, combinations
import sys
input = sys.stdin.readline

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
    n, m, k = map(int, input().split())
    g = [[-1] * n for _ in range(n)]
    u, v, w = [0] * m, [0] * m, [0] * m
    for i in range(m):
        u[i], v[i], w[i] = map(int, input().split())
        u[i] -= 1
        v[i] -= 1
        g[u[i]][v[i]] = w[i]
        g[v[i]][u[i]] = w[i]
    

    ans = []
    for p in combinations(range(m), n - 1):
        uf = UnionFind(n)
        cost = 0
        for i in p:
            if not uf.same(u[i], v[i]):
                uf.merge(u[i], v[i])
                cost += w[i]
        par = set()
        for i in range(n):
            par.add(uf.leader(i))
        if len(par) == 1:
            ans.append(cost % k)
    
    print(min(ans))


if __name__ == "__main__":
    main()