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


def main() -> None:
    N, M = map(int, input().split())

    UF = UnionFind(N)

    for _ in range(m):
        A, B = map(lambda x: int(x) - 1,input().split())
        UF.merge(A, B)

    ans = 0
    for i in range(N):
        ans = max(ans, UF.size(i))

    print(ans)


if __name__ == "__main__":
    main()

N, Q = 0, 0
mincost = 0
v = []
v2 = []

def calcmincost():
    global v
    res = 0
    d = dsu.DSU(N)
    v.sort()
    for c, a, b in v:
        if d.same(a, b):
            continue
        d.merge(a, b)
        res += c
    return res

def solve():
    global mincost, v2
    mincost = calcmincost()
    d = [dsu.DSU(N) for _ in range(11)]
    
    for c, a, b in v:
        for i in range(10, c - 1, -1):
            d[i].merge(a, b)

    for w, u, v in v2:
        flg = -1
        for i in range(11):
            if d[i].same(u, v):
                flg = i
                break
        for i in range(10, w - 1, -1):
            d[i].merge(u, v)

        diff = max(0, flg - w)
        mincost -= diff
        print(mincost)

def main():
    global N, Q, v, v2
    N, Q = map(int, input().split())
    v = []
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        v.append((c, a, b))
    v2 = []
    for _ in range(Q):
        x, y, z = map(int, input().split())
        x -=1
        y -= 1
        v2.append((z, x, y))
    solve()

if __name__=='__main__':
    main()