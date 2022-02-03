import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)

memo = [0] * n
done = [False] * n

def dp(v: int) -> int:
    if done[v]: return memo[v]
    num = 0
    for i in g[v]:
        num = max(num, dp(i) + 1)

    done[v] = True
    memo[v] = num
    return num

ans = 0
for i in range(n):
    ans = max(ans, dp(i))

print(ans)