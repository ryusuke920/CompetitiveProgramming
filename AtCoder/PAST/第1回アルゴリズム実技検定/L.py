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


from itertools import product
from collections import defaultdict

def main() -> None:
    N, M = map(int, input().split())
    l1 = [list(map(int, input().split())) for _ in range(N)]
    l2 = [list(map(int, input().split())) for _ in range(M)]

    ans = 10**18

    # 小さい塔の bit全探索
    for i in product([0, 1], repeat=M):
        # 立っている bit の数を探索
        cnt = 0
        d = defaultdict(int)
        for j in range(M):
            if i[j] == 1:
                cnt += 1
                d[j] = N + cnt - 1
                
        
        g = []
        for ii in range(N):
            for jj in range(N):
                if ii == jj:
                    continue
                x_i, y_i, c_i = l1[ii]
                x_j, y_j, c_j = l1[jj]
                dist = ((x_i - x_j) ** 2 + (y_i - y_j) ** 2)**0.5
                if c_i != c_j:
                    dist *= 10
                g.append((ii, jj, dist))

        for ii in range(M):
            for jj in range(M):
                if ii == jj:
                    continue
                if not (i[ii] and i[jj]):
                    continue
                x_i, y_i, c_i = l2[ii]
                x_j, y_j, c_j = l2[jj]
                dist = ((x_i - x_j) ** 2 + (y_i - y_j) ** 2)**0.5
                if c_i != c_j:
                    dist *= 10
                g.append((d[ii], d[jj], dist))
        
        for ii in range(N):
            for jj in range(M):
                if not i[jj]:
                    continue
                x_i, y_i, c_i = l1[ii]
                x_j, y_j, c_j = l2[jj]

                dist = ((x_i - x_j) ** 2 + (y_i - y_j) ** 2)**0.5
                if c_i != c_j:
                    dist *= 10
                g.append((ii, d[jj], dist))
        ans = min(ans, sum(Kruskal(N + cnt, g).cost(g)))

    print(ans)


if __name__ == "__main__":
    main()