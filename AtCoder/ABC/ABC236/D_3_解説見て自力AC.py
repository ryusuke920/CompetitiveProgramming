import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
a = [[0] * (i + 1) + list(map(int, input().split())) for i in range(2 * n - 1)]

def dfs(bool: list, cnt: int) -> None:
    global ans

    # 終了するかどうかを確認する
    start = -1
    for i in range(2 * n):
        if bool[i]:
            start = i
            break
    
    # 終了するときの処理
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