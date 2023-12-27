import sys
sys.setrecursionlimit(500_000)

def dfs(now: int, prev: int) -> None:
    for nxt in g[now]:
        if prev == nxt:
            continue
        dfs(nxt, now)
        dp[now] += dp[nxt]

def main() -> None:
    global g, dp

    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        g[b].append(a)
    
    dp = [1] * n
    dfs(0, -1)

    print(n * (n - 1) * (n - 2) // 6 - (sum([dp[i] * (n - dp[i]) for i in range(n)]) - n * (n - 1) // 2))


if __name__ == "__main__":
    main()