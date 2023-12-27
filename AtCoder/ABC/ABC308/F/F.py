import sys

N = int(input())
A = list(map(int, input().split()))
S = input()
m = [[] for _ in range(3)]
x = [[] for _ in range(3)]

def mex(a, b, c):
    v = [a, b, c]
    v.sort()
    ans = 0
    for i in v:
        if i == ans:
            ans += 1
    return ans

def solve():
    for i in range(3):
        x[i] = [0] * (N + 1)
        m[i] = [0] * (N + 1)
    for i in range(N):
        if S[i] == 'M':
            m[A[i]][i+1] += 1
        elif S[i] == 'X':
            x[A[i]][i+1] += 1
    for i in range(3):
        for j in range(N):
            m[i][j+1] += m[i][j]
            x[i][j+1] += x[i][j]
    ans = 0
    for i in range(N):
        if S[i] == 'E':
            for l in range(3):
                for r in range(3):
                    ans += mex(A[i], l, r) * (m[l][i] - m[l][0]) * (x[r][N] - x[r][i+1])
                    print(mex(A[i], l, r))
    print(ans)

if __name__ == "__main__":
    solve()
