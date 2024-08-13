class Kruskal:
    def __init__(self, n: int, g: list) -> None:
        self.n = n
        self.g = g.sort(key=lambda x: x[2])
        self.p = [-1] * n


    def leader(self, a: int) -> int:
        while self.p[a] >= 0:
            a = self.p[a]

        return a


    def merge(self, a: int, b: int) -> int:
        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if self.p[x] > self.p[y]:
            x, y = y, x

        self.p[x] += self.p[y]
        self.p[y] = x

        return x


    def same(self, a: int, b: int) -> bool:
        return self.leader(a) == self.leader(b)


    def size(self, a: int) -> int:
        return -self.p[self.leader(a)]


    def cost(self, g: list) -> list:
        tree = []
        for u, v, cost in g:
            if self.same(u, v):
                continue
            self.merge(u, v)
            tree.append(cost)

        return tree


class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.p = [-1] * n


    def leader(self, a: int) -> int:
        while self.p[a] >= 0:
            a = self.p[a]
        return a


    def merge(self, a: int, b: int) -> int:
        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if self.p[x] > self.p[y]:
            x, y = y, x

        self.p[x] += self.p[y]
        self.p[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        return self.leader(a) == self.leader(b)

    def groups(self) -> list:
        member = [[] for _ in range(self.n)]
        for i in range(self.n):
            member[self.leader(i)].append(i)
        return member

    def size(self, a: int) -> int:
        return -self.p[self.leader(a)]



from itertools import product
from collections import defaultdict

def main() -> None:
    N, M = map(int, input().split())
    uf = UnionFind(N)
    g = []
    l = []
    ans = 0
    for _ in range(M):
        K, C = map(int, input().split())
        A = list(map(lambda x: int(x) - 1, input().split()))
        l.append([K, C] + A)
    l.sort(key=lambda x: x[1])
    # print(*l, sep="\n")
    for i in range(M):
        K, C, *A = l[i]
        # print(i, C, A)
        for j in range(K - 1):
            if uf.same(A[j], A[j + 1]):
                continue
            uf.merge(A[j], A[j + 1])
            ans += C
    
    t = uf.groups()
    cnt = 0
    for i in t:
        if len(i) != 0:
            cnt += 1
    if cnt != 1:
        exit(print(-1))
    
    print(ans)

    # ans = sum(Kruskal(N, g).cost(g))
    # print(ans)


if __name__ == "__main__":
    main()