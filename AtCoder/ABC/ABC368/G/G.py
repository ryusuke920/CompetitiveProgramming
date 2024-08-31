class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (2 * n)
        self.lazy_add = [0] * n
        self.lazy_mul = [1] * n

    def _apply(self, p, value_add, value_mul):
        self.data[p] = self.data[p] * value_mul + value_add
        if p < self.n:
            self.lazy_mul[p] *= value_mul
            self.lazy_add[p] = self.lazy_add[p] * value_mul + value_add

    def _build(self, p):
        while p > 1:
            p //= 2
            self.data[p] = max(self.data[2 * p], self.data[2 * p + 1])
            self.data[p] = self.data[p] * self.lazy_mul[p] + self.lazy_add[p]

    def _push(self, p):
        for s in range(self.n.bit_length(), 0, -1):
            i = p >> s
            if self.lazy_mul[i] != 1 or self.lazy_add[i] != 0:
                self._apply(2 * i, self.lazy_add[i], self.lazy_mul[i])
                self._apply(2 * i + 1, self.lazy_add[i], self.lazy_mul[i])
                self.lazy_mul[i] = 1
                self.lazy_add[i] = 0

    def update(self, l, r, value_add, value_mul):
        l += self.n
        r += self.n + 1
        l0, r0 = l, r

        while l < r:
            if l & 1:
                self._apply(l, value_add, value_mul)
                l += 1
            if r & 1:
                r -= 1
                self._apply(r, value_add, value_mul)
            l //= 2
            r //= 2

        self._build(l0)
        self._build(r0 - 1)

    def query(self, l, r):
        l += self.n
        r += self.n + 1
        self._push(l)
        self._push(r - 1)

        res = 0
        while l < r:
            if l & 1:
                res = max(res, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.data[r])
            l //= 2
            r //= 2
        return res

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())
    
    seg_tree_A = SegmentTree(N)
    seg_tree_B = SegmentTree(N)
    
    # 初期値の設定
    for i in range(N):
        seg_tree_A.update(i, i, A[i], 1)
        seg_tree_B.update(i, i, B[i], 1)
    
    ans = []
    
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            i = query[1] - 1
            x = query[2]
            seg_tree_A.update(i, i, x - A[i], 1)
            A[i] = x
        elif query[0] == 2:
            i = query[1] - 1
            x = query[2]
            seg_tree_B.update(i, i, x - B[i], 1)
            B[i] = x
        elif query[0] == 3:
            l = query[1] - 1
            r = query[2] - 1
            v = 0
            for i in range(l, r + 1):
                A_i = seg_tree_A.query(i, i)
                B_i = seg_tree_B.query(i, i)
                v = max(v + A_i, v * B_i)
            ans.append(v)
    
    for i in ans:
        print(i)

solve()