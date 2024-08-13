'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc358/tasks/abc358_g
oj t -c "python3 G.py"
oj s https://atcoder.jp/contests/abc358/tasks/abc358_g G.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    H, W, K = map(int, input().split())
    sy, sx = map(lambda x: int(x) - 1, input().split())
    # A = [list(map(lambda x: int(x) -, input().split())) for _ in range(H)]
    A = [list(map(int, input().split())) for _ in range(H)]
    N = 2000
    INF = 10**18
    dp = [[[-INF]*50 for _ in range(50)] for _ in range(N + 1)]
    INF = 10**18
    dp[0][sy][sx] = 0
    d = ((0, 1), (0, -1), (1, 0), (-1, 0), (0, 0))
    for i in range(N):
        for y in range(H):
            for x in range(W):
                for dy, dx in d:
                    ny = y + dy
                    nx = x + dx
                    if not (0 <= ny < H and 0 <= nx < W):
                        continue
                    # cnt = A[ny][nx] + dp[i + 1][ny][nx]
                    dp[i + 1][ny][nx] = max(dp[i + 1][ny][nx], dp[i][y][x] + A[ny][nx])
    
    ans = 0
    if N < K:
        for i in range(H):
            for j in range(W):
                ans = max(ans, dp[N][i][j] + A[i][j]*(K - N))
    else:
        for i in range(H):
            for j in range(W):
                ans = max(ans, dp[K][i][j])
    print(ans)


if __name__ == "__main__":
    main()