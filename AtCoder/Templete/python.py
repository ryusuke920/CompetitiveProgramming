from math import sin, cos, tan, degrees, sqrt
from collections import defaultdict, deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
from heapq import heappush, heappop
from bisect import bisect, bisect_left, bisect_right

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin

def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LC(): return list(input())
def IC(): return [int(i) for i in input()]
def MI(): return map(int, sys.stdin.readline().split())

###########################################################################################
# 配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ
def OrMore(K: int, A: list) -> int:
    "-1の時は解が無い時"
    return len(A) - bisect_left(A, K), (bisect_left(A, K) if bisect_left(A, K) <= len(A) - 1 else -1)

###########################################################################################
# 配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ
def OrLessThan(K: int, A: list) -> int:
    "-1の時は解が無い時"
    return bisect_right(A, K), (-1 if bisect_right(A, K) == 0 else bisect_right(A, K) - 1)

###########################################################################################
# 配列Aの中のうち、kより大きいものの個数と始まりの0indexを返すライブラリ
def More(K: int, A: list) -> int:
    "-1の時は解が無い時"
    return len(A) - bisect_right(A, K), (bisect_right(A, K) if bisect_right(A, K) <= len(A) - 1 else -1)

###########################################################################################
# 配列Aの中のうち、k未満の個数と終わりの0indexを返すライブラリ
def LessThan(K: int, A: list) -> int:
    "-1の時は解が無い時"
    return bisect_left(A, K), (-1 if bisect_left(A, K) == 0 else bisect_left(A, K) - 1)

###########################################################################################
# 二分探索
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    return

def binary_search(left, right):
    while abs(left - right) > 1:
        mid = (left + right) // 2
        if is_ok(mid):
            left = mid
        else:
            right = mid
    return left # Trueの方を返す？

###########################################################################################
# 座標圧縮
def CC(A: list) -> list:
    B = {j: i + 1 for i, j in enumerate(set(A))}
    return B

###########################################################################################
# ダイクストラ法
def dijkstra(s, graph): # (始点, グラフのリスト)
    INF = 10 ** 18
    dist = [INF] * len(graph) # INF で初期化
    check = [False] * len(graph) # Bool
    dist[s] = 0
    q = [(0, s)] # （距離・ノード）
    while q:
        v = heappop(q)[1] # 今いるノード
        if check[v]: continue # すでに行っていたらcontinue
        check[v] = True # 訪問済み
        for i, j in graph[v]: # 先のノード・距離
            if check[i] != False: continue
            if dist[i] <= dist[v] + j: continue
            dist[i] = dist[v] + j
            heappush(q, (dist[i], i)) # 必ず[0]が距離になるように（優先度付きキュー）
    return dist

###########################################################################################
# ダブリング
class Doubling():
    def __init__(self, n, k_max, f) -> None:
        """要素数nのダブリングテーブルを作成します。"""

        k_bits = k_max.bit_length()

        # dub[i][j] = 値jを2**i回操作した結果
        dub = [[0] * n for _ in range(k_bits)]

        # 1回(2**0回)操作した結果を作成
        for j in range(n):
            dub[0][j] = f(j)

        # 2**i回操作した結果を順に作成
        # 2**(i-1)回操作を2回すれば2**i回操作したことになる
        for i in range(1, k_bits):
            for j in range(n):
                dub[i][j] = dub[i - 1][dub[i - 1][j]]

        self.doubling_table = dub

    def get(self, x, k):
        """xをk回操作した値を取得します。"""
        # kをビットごとに分解して、2**a + 2**b + 2**c + ... の形で考える。
        # xを2**a回操作した結果を2**b回操作した結果を2**c回操作… のように順に適用する
        now = x
        for i in range(k.bit_length()):
            if k>>i & 1:
                now = self.doubling_table[i][now]

        return now

def calc():
    "関数を定義する"
    return

###########################################################################################
# 拡張ユークリッドの互除法
def extgcd(a: int, b: int) -> int:
    "ax + by = gcd(a,b) = d となる (x, y, d) を返す"
    if b == 0:
        return (1, 0, a)

    q, r = a // b, a % b
    x, y, d = extgcd(b, r)
    s, t = y, x - q * y

    return s, t, d # (qb + r)s + bt = dとなる s, t, d

###########################################################################################
# LCSの文字列を求める
def LCS(S, T):
    L1 = len(S)
    L2 = len(T)
    dp = [[0] * (L2 + 1) for i in range(L1 + 1)]

    for i in range(L1 - 1, -1, -1):
        for j in range(L2 - 1, -1, -1):
            r = max(dp[i + 1][j], dp[i][j + 1])
            if S[i] == T[j]:
                r = max(r, dp[i + 1][j + 1] + 1)
            dp[i][j] = r
    # dp[0][0] が長さの解

    # ここからは復元処理
    res = []
    i = 0; j = 0
    while i < L1 and j < L2:
        if S[i] == T[j]:
            res.append(S[i])
            i += 1; j += 1
        elif dp[i][j] == dp[i + 1][j]:
            i += 1
        elif dp[i][j] == dp[i][j + 1]:
            j += 1
    return "".join(res)

###########################################################################################
# LISを求める
def LIS(A, N): # 配列・長さ
    INF = 10 ** 18
    dp = [INF] * N
    for i in A:
        x = bisect_left(dp, i)
        dp[x] = i
    return(bisect_left(dp, INF))

###########################################################################################
# 素因数分解
def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

###########################################################################################
# 素数判定
def PrimaryCheck(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
            break
    return True

###########################################################################################
# nCkを求める
def combination(n, k):
    nCk = under = top = 1
    mod = 10 ** 9 + 7

    # 分母
    for i in range(2, k + 1):
        under *= i
        under %= mod

    # 分子
    for i in range(k):
        top *= (n - i)
        top %= mod

    nCk = top * pow(under, mod - 2, mod)

    return nCk % mod

###########################################################################################
# エラトステネスの篩
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]: continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

###########################################################################################
# 約数列挙
def divisors(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)

    divisor.sort()
    return divisor

###########################################################################################
# 部分累積和を求める
def MaxCumulativeSum(num_array, k): # 配列・区間幅
    max_cumulative_sum = [] # 区間幅分の部分和を格納する配列
    count = 0
    for i in range(k):
       count += num_array[i]
    max_cumulative_sum.append([count, 0, 0 + k]) # 部分和・左端・右端
    
    for i in range(len(num_array) - k):
        count += num_array[i + k]
        count -= num_array[i]
        max_cumulative_sum.append([count, i + 1, i + 1 + k])
    
    max_cumulative_sum.sort(key = lambda x: x[0], reverse = True) # 降順にソート
    return max_cumulative_sum[0]

###########################################################################################
# 0~NまでのXorを求める
def XorToN(N: int) -> int:
    if N % 4 == 0:
        return N
    elif N % 4 == 1:
        return 1
    elif N % 4 == 2:
        return N + 1
    elif N % 4 == 3:
        return 0

###########################################################################################
# 

###########################################################################################
# SCC(強連結成分分解)
class SCC:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.rev_graph = [[] for _ in range(n)]
        self.labels = [-1] * n
        self.lb_cnt = 0

    def add_edge(self, v, nxt_v):
        self.graph[v].append(nxt_v)
        self.rev_graph[nxt_v].append(v)

    def build(self):
        self.post_order = []
        self.used = [False] * self.n
        for v in range(self.n):
            if not self.used[v]:
                self._dfs(v)
        for v in reversed(self.post_order):
            if self.labels[v] == -1:
                self._rev_dfs(v)
                self.lb_cnt += 1

    def _dfs(self, v):
        stack = [v, 0]
        while stack:
            v, idx = stack[-2:]
            if not idx and self.used[v]:
                stack.pop()
                stack.pop()
            else:
                self.used[v] = True
                if idx < len(self.graph[v]):
                    stack[-1] += 1
                    stack.append(self.graph[v][idx])
                    stack.append(0)
                else:
                    stack.pop()
                    self.post_order.append(stack.pop())

    def _rev_dfs(self, v):
        stack = [v]
        self.labels[v] = self.lb_cnt
        while stack:
            v = stack.pop()
            for nxt_v in self.rev_graph[v]:
                if self.labels[nxt_v] != -1:
                    continue
                stack.append(nxt_v)
                self.labels[nxt_v] = self.lb_cnt

    def construct(self):
        self.dag = [[] for i in range(self.lb_cnt)]
        self.groups = [[] for i in range(self.lb_cnt)]
        for v, lb in enumerate(self.labels):
            for nxt_v in self.graph[v]:
                nxt_lb = self.labels[nxt_v]
                if lb == nxt_lb:
                    continue
                self.dag[lb].append(nxt_lb)
            self.groups[lb].append(v)
        return self.dag, self.groups

###########################################################################################
# Union Find木
"""
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x,y):
    return find(x) == find(y)

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y

par = [i for i in range(n)]
"""
###########################################################################################
# 遅延評価セグメント木
"""
〜segfuncの使い方について〜
update(k, x): k番目の要素をxに更新する
query(l, r): [l, r)（l <= k < r の区間）から値kを取得する
"""
def segfunc(x: int, y: int) -> int:
    "ここで求めたい処理を行う, max(x, y) や x ^ y など"
    return x ^ y

"""
〜単位元の一覧について〜
最小値：float("inf")
最大値：-float("inf")
XOR：0
区間和：0
区間積：1
最大公約数：0
"""
ide_ele = 0 # 初期値（単位元）の設定

class LazySegmentTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.data = [ide_ele] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        for i in range(n):
            self.data[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def gindex(self, l, r):
        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while l < r:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.data[2 * i] = v
            self.data[2 * i + 1] = v
            self.lazy[i] = None

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

    def query(self, l, r):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res

# わからなくなったら典型90問の29を参考にすること

###########################################################################################
# warshall_floyd法
"""
def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
"""
###########################################################################################
# 初期値宣言
INF = 10 ** 20
mod = 10 ** 9 + 7
ma = 10 ** 20
mi = -10 ** 20

###########################################################################################
# 以下、問題ごとのコード
def solve():

    return
solve()