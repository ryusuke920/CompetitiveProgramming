N, K = map(int, input().split())
A = [0]*(max(N, K) + 1)
mod = 10**9
for i in range(K):
    A[i] = 1

cnt = sum(A[:K])
A[K] = cnt

for i in range(K + 1, N + 1):
    cnt -= A[i - K - 1]
    cnt += A[i - 1]
    A[i] = cnt
    A[i] %= mod

print(A[N])