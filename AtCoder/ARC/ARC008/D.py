"""
〜segfuncの使い方について〜
update(k, x): k番目の要素をxに更新する
query(l, r): [l, r)（l <= k < r の区間）から値kを取得する
"""

class LazySegmentTree:
    def __init__(self, box, data, start): # 箱の中身, データの数・木？, 初期値(1, 0)
        self.num = len(box) # 箱の数
        self.n = 1 << (n - 1).bit_length()
        self.node = [e] * 2 * n
        self.data = data
        self.lazy = [None] * 2 * self.num
        self.e = e
        for i in range(n):
            self.node[self.n + i] = box[i]
        for i in range(self.n - 1, 0, -1):
            self.node[i] = self.data(self.node[2 * i], self.node[2 * i + 1])

    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.data[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.data[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def sum(self,l,r):
        vl, vr = self.e, self.e
        l += self.n
        r += self.n
        while(l < r):
            if(l % 2 == 1):
                vl = self.data(vl, self.node[l])
                l += 1
            l //= 2
            if(r % 2 == 1):
                r -= 1
                vr = self.data(self.node[r], vr)
            r //= 2
        return self.data(vl, vr)

# わからなくなったら典型90問の29を参考にすること
n, m = map(int,input().split())
p, a, b = [], [], []
for i in range(m):
    P, A, B = map(str,input().split())
    p.append(int(P))
    a.append(float(A))
    b.append(float(B))

e = (1, 0) # 単位元?
data = lambda a, b: (a[0] * b[0], a[1] * b[0] + b[1])
start = e
box = [e] * n
seg = LazySegmentTree(box, data, start) # 箱の中身, データの数・木？, 初期値(1, 0)

# 座標圧縮
z = {j: i for i, j in enumerate(set(p))}
print("座圧 =", z)
ans = [1]

for i in range(m):
    index = p[i]
    j = z[index]
    seg.update()
    ans.append(sum(seg.sum(0, n)))
print(ans)