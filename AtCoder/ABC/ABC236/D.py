import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
a = [[0] * (i + 1) + list(map(int, input().split())) for i in range(2 * n - 1)]

def dfs(bool: bool, cnt: int) -> None:

    global ans

    start = -1
    # 終了条件
    for i in range(2 * n):
        if bool[i]:
            start = i
            break

    if start == -1:
        ans = max(ans, cnt)
        return

    bool[start] = False
    for i in range(start + 1, 2 * n):
        if bool[i]:
            bool[i] = False
            dfs(bool, cnt ^ a[start][i])
            bool[i] = True
    bool[start] = True

ans = 0
dfs([True] * 2 * n, 0)

print(ans)