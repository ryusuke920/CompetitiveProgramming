from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)

N = int(stdin.readline().strip())
G = [[] for _ in range(N)]
C = [0]*N
dp = [[0]*2 for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, stdin.readline().strip().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

C = list(map(int, stdin.readline().strip().split()))

def dfs(now, par):
    dp[now][0] = C[now]
    dp[now][1] = 0
    for to in G[now]:
        if to == par:
            continue
        dfs(to, now)
        dp[now][0] += dp[to][0]
        dp[now][1] += dp[to][0] + dp[to][1]

ans = 10**18

def dfs2(now, par, Csum, AnsSum):
    global ans
    tmpCsum = Csum
    CurAns = Csum + AnsSum
    for to in G[now]:
        if to == par:
            continue
        CurAns += dp[to][0] + dp[to][1]
    ans = min(ans, CurAns)
    for to in G[now]:
        if to == par:
            continue
        Csum += dp[to][0]
        AnsSum += dp[to][0] + dp[to][1]
    Csum += C[now]
    for to in G[now]:
        if to == par:
            continue
        nextCsum = Csum - dp[to][0]
        dfs2(to, now, nextCsum, AnsSum - (dp[to][0] + dp[to][1]) + tmpCsum)

dfs(0, -1)
ans = dp[0][1]
dfs2(0, -1, 0, 0)
print(ans)