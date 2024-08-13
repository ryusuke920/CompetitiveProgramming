def query(start, diff, cur):
    cur -= start
    if cur % diff == 0:
        return cur // diff
    return -1

def count2(A, start, diff, ans, N):
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        q = query(start, diff, A[i])
        if 0 <= q < N:
            dp[q + 1] += dp[q]
            dp[q + 1] %= MOD
    for i in range(N + 1):
        ans[i] += dp[i]
        ans[i] %= MOD

def solve(N, A):
    fac, fac_inv = calc_facinv(505050)
    ans = [0] * 1000
    s = set()
    for i in range(N):
        for j in range(i, N):
            s.add((A[i], A[j] - A[i]))
    
    count_map = {}
    for num in A:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    for start, diff in s:
        if diff == 0:
            for i in range(1, count_map[start] + 1):
                ans[i] += combination(count_map[start], i, fac, fac_inv)
                ans[i] %= MOD
            continue
        count2(A, start, diff, ans, N)

    ans[1] = N
    print(" ".join(str(ans[i]) for i in range(1, N + 1)))



N = int(input())
A = list(map(int, input().split()))
solve(N, A)