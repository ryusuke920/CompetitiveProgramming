'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc268/tasks/abc268_f
oj t -c "python3 F.py"
oj s https://atcoder.jp/contests/abc268/tasks/abc268_f F.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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


def dfs(now: int, pre: int):
    global p
    if visited[now]:
        p = now
        return
    
    visited[now] = True
    for nxt in edge[now]:
        if pre == nxt:
            continue
        dfs(nxt, now)

def rev_dfs(now: int, pre: int, l: set):
    global cnt, p, cycle

    for nxt in edge[now]:
        if nxt == pre:
            continue
        if nxt == p:
            for i in l:
                cycle.add(i)
            cycle.add(p)
            return
        l.add(nxt)
        rev_dfs(nxt, now, l)
        l.remove(nxt)

n = int(input())

edge = [[] for _ in range(n)]
uv = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]
for i in range(n):
    u, v = uv[i]
    edge[u].append(v)
    edge[v].append(u)

visited = [False] * n
p = -1
dfs(0, -1)

cnt = 0
cycle = set()
rev_dfs(p, -1, set())

#print(cycle)
uf = UnionFind(n)
for i in range(n):
    u, v = uv[i]
    if u in cycle and v in cycle:
        continue
    uf.merge(u, v)


q = int(input())
for _ in range(q):
    x, y = map(lambda x: int(x) - 1, input().split())
    if uf.same(x, y):
        print('Yes')
    else:
        print('No')

