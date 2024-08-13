from bisect import bisect_left

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    dp = [float('inf')] * (N + 1)
    ans = [0] * N
    dp[0] = -float('inf')

    for i in range(N - 1, -1, -1):
        pos = bisect_left(dp, A[i])
        if dp[pos - 1] < A[i] and A[i] < dp[pos]:
            dp[pos] = A[i]
            ans[i] = 1

    cnt = dp.count(float('inf'))
    length = len(dp) - cnt - 1
    for i in range(N):
        if ans[i] and length > 0:
            ans[i] = length
            length -= 1
        else:
            ans[i] = 0

    print(ans.count(0), * [i + 1 for i in range(N) if ans[i] == 0], sep=' ')