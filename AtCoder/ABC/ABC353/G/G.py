import sys
input = sys.stdin.readline


import sys

class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])
    
    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1
    
    def get(self, p):
        return self._d[p + self._size]

    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    def all_prod(self):
        return self._d[1]
    
    def max_right(self, l, f):
        if l == self._n: return self._n
        l += self._size
        sm = self._e()
        while True:
            while l % 2 == 0: l >>= 1
            if not f(self._op(sm, self._d[l])):
                while l < self._size:
                    l <<= 1
                    if f(self._op(sm, self._d[l])):
                        sm = self._op(sm, self._d[l])
                        l += 1
                return l - self._size
            sm = self._op(sm, self._d[l])
            l += 1
            if l & -l == l: break
        return self._n

def op(x, y):
    return max(x, y)

def e():
    return [-INF, -INF]

# n, q = map(int, input().split())
# A = list(map(int, input().split()))
# seg = SegTree(op, e, n, A)
# for _ in range(q):
#     t, a, b = map(int, input().split())
#     a -= 1
#     if t == 1:
#         seg.set(a, b)
#     elif t == 2:
#         print(seg.prod(a, b))
#     else:
#         f = lambda x: x < b
#         print(seg.max_right(a, f) + 1)


N, C = map(int, input().split())
M = int(input())
T, P = [0]*M, [0]*M
for i in range(M):
    T[i], P[i] = map(int, input().split())
    T[i] -= 1

INF = 10**18
p1 = [[0]*2 for _ in range(N)]
p2 = [[0]*2 for _ in range(N)]
for i in range(1, N):
    p1[i][0] = -INF
    p2[i][0] = -INF
    p1[i][1] = i
    p2[i][1] = i

seg1 = SegTree(op, e, N, p1)
seg2 = SegTree(op, e, N, p2)
for i in range(M):
    left = seg1.prod(0, T[i] + 1)
    right = seg2.prod(T[i], N)
    left[0] = left[0] - left[1]*C - abs(T[i] - left[1])*C
    right[0] = right[0] + right[1]*C - abs(T[i] - right[1])*C
    
    mid = max(left, right)
    mid[0] += P[i]
    mid[1] = T[i]
    left = mid
    left[0] += T[i]*C
    right = mid
    right[0] -= T[i]*C
    seg1.set(T[i], max(seg1.get(T[i]), left))
    seg2.set(T[i], max(seg2.get(T[i]), right))

ans = 0
for i in range(N):
    x = seg1.get(i)
    x[0] -= x[1]*C
    ans = max(ans, x[0])

print(ans)