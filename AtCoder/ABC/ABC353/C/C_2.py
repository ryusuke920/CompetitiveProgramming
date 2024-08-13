from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))

S = [0]*(N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

ans = 0
for i in range(N):
    ans += S[N] - S[i + 1] + A[i]*(N - i - 1)
    p = bisect_left(A, 10**8 - A[i])
    ans -= 10**8 * (N - max(i + 1, p))
    print(i, ans)

print(ans)