'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc264/tasks/abc264_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc264/tasks/abc264_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

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

import sys
input = sys.stdin.readline

def main() -> None:
    n, m, e = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(e)]
    q = int(input())
    x = [int(input()) for _ in range(q)][::-1]

    is_ok = set()
    ans = 0
    num = []
    uf = UnionFind(n + m + 10)
    cnt = set([i + 1 for i in range(n + m)])
    for i in x:
        cnt ^= set([i])


    for i in list(cnt):
        u, v = t[i - 1]
        if u > n and v > n:
            uf.merge(u, v)
        if u <= n and v > n:
            if u not in is_ok:
                is_ok.add(u)
                ans += 1
                uf.merge(u, v)
        if u <= n and v <= n:
            if u not in is_ok and v not in is_ok:
                uf.merge(u, v)
            elif u not in is_ok or v not in is_ok:
                if u in is_ok:
                    is_ok.add(v)
                    ans += 1
                    uf.merge(u, v)
                if v in is_ok:
                    is_ok.add(v)
                    ans += 1
                    uf.merge(u, v)
    
    print(ans, num)

    for i in range(q):
        num.append(ans)
        u, v = t[x[i] - 1]
        if u > n and v > n:
            uf.merge(u, v)
        if u <= n and v > n:
            if u not in is_ok:
                is_ok.add(u)
                ans += 1
                uf.merge(u, v)
        if u <= n and v <= n:
            if u not in is_ok and v not in is_ok:
                uf.merge(u, v)
            elif u not in is_ok or v not in is_ok:
                if u in is_ok:
                    is_ok.add(v)
                    ans += 1
                    uf.merge(u, v)
                if v in is_ok:
                    is_ok.add(v)
                    ans += 1
                    uf.merge(u, v)
        
    print(num[::-1])
    for i in num[::-1]:
        print(i)
 

if __name__ == "__main__":
    main()