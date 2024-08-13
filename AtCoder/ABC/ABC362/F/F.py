import sys
input = sys.stdin.readline

def calc_facinv(n: int) -> list:
    '逆元テーブルを作成する'

    # 階乗テーブルの作成

    fac[0] = 1
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i
        fac[i] %= mod
    
    # 逆元テーブルの作成

    fac_inv[0] = 1
    for i in range(1, n + 1):
        fac_inv[i] = pow(fac[i], mod - 2, mod)
    
    return fac, fac_inv

def combination(n: int, k: int) -> int:
    '''nCkを計算する'''
    if n < 0 or k < 0 or n < k:
        return 0

    return fac[n] * fac_inv[k] * fac_inv[n - k] % mod


def f(i: int, j: int) -> None:
    dp = [0] * (N + 1)
    dp[0] = 1
    for k in range(N):
        num = A[k] - i
        if num % j == 0:
            q = num // j
        else:
            q = -1
        if 0 <= q < N:
            dp[q + 1] += dp[q]
            dp[q + 1] %= mod

    for k in range(N + 1):
        ans[k] += dp[k]
        ans[k] %= mod


def suffix_array_construction(s):
    n = len(s)
    suffix_array = sorted(range(n), key=lambda i: s[i:])
    rank = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    k = 1
    while k < n:
        suffix_array = sorted(range(n), key=lambda i: (rank[i], rank[(i + k) % n]))
        new_rank = [0] * n
        for i in range(1, n):
            prev = suffix_array[i - 1]
            curr = suffix_array[i]
            new_rank[curr] = new_rank[prev]
            if rank[curr] != rank[prev] or rank[(curr + k) % n] != rank[(prev + k) % n]:
                new_rank[curr] += 1
        rank = new_rank
        k *= 2
    return suffix_array

def lcp_array_construction(s, suffix_array):
    n = len(s)
    rank = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    lcp_array = [0] * (n - 1)
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp_array[rank[i] - 1] = h
            if h > 0:
                h -= 1
    return lcp_array

def process_queries_with_suffix_array(s, queries):
    suffix_array = suffix_array_construction(s)
    lcp_array = lcp_array_construction(s, suffix_array)
    results = []
    n = len(s)
    for t in queries:
        m = len(t)
        l, r = 0, n

        while l < r:
            mid = (l + r) // 2
            if s[suffix_array[mid]:].startswith(t):
                r = mid
            else:
                l = mid + 1
        left = l

        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if s[suffix_array[mid]:].startswith(t):
                l = mid + 1
            else:
                r = mid
        right = l
        results.append(right - left)
    return results

N = int(input())
A = list(map(int, input().split()))
mod = 998244353
fac = [0] * 101010
fac_inv = [0] * 101010
calc_facinv(101000)
ans = [0] * 1000

s = set()
for i in range(N):
    for j in range(i, N):
        s.add((A[i], A[j] - A[i]))

d = {}
for i in A:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i, j in s:
    if j == 0:
        for k in range(1, d[i] + 1):
            ans[k] += combination(d[i], k)
            ans[k] %= mod
        continue
    f(i, j)

ans[1] = N
print(*ans[1:N + 1])