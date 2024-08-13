import sys

def dfs(bit, turn):
    if dp[bit] != -1:
        return dp[bit]
    else:
        for i in range(N):
            for j in range(i + 1, N):
                if bit & (1 << i) == 0 and bit & (1 << j) == 0 and (A[i] == A[j] or B[i] == B[j]):
                    if dfs(bit | (1 << i) | (1 << j), turn ^ 1) == turn:
                        dp[bit] = turn
                        return turn
        dp[bit] = turn ^ 1
        return dp[bit]

N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [-1 for _ in range(1 << N)]
ans = dfs(0, 0)

if ans == 0:
    print("Takahashi")
else:
    print("Aoki")