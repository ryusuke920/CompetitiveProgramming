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

import sys
input = sys.stdin.readline

from collections import deque, defaultdict

def main() -> None:
    N, M, K = map(int, input().split())
    INF = 10**18
    # 偶奇が異なれば exit
    if N % 2 != K % 2:
        exit(print("No"))
    if N * M < K:
        exit(print("No"))
    
    G = [[-INF]*M for _ in range(N)]
    x, y = 0, M - 1
    G[x][y] = 1
    gx, gy = N - 1, M - 1
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    while x != gx or y != gy:
        pre_x, pre_y = x, y
        dist = abs(x - gx) + abs(y - gy) + G[x][y]
        
        if dist <= K:
            for dy, dx in d:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                if G[nx][ny] == -INF:
                    if abs(nx - gx) + abs(ny - gy) + G[x][y] + 1 > dist:
                        x = nx
                        y = ny
                        G[x][y] = G[pre_x][pre_y] + 1
                        break
        
        if x == pre_x and y == pre_y:
            for dy, dx in d:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                if G[nx][ny] == -INF:
                    x = nx
                    y = ny
                    G[x][y] = G[pre_x][pre_y] + 1
                    break
        
        if x == pre_x and y == pre_y:
            break
    
    if G[N - 1][M - 1] == -INF:
        exit(print("No"))

    S = [["+"] * (M * 2 + 1) for _ in range(N * 2 + 1)]

    for i in range(N):
        for j in range(M - 1):
            if abs(G[i][j + 1] - G[i][j]) == 1:
                S[i * 2 + 1][j * 2 + 2] = "."
            else:
                S[i * 2 + 1][j * 2 + 2] = "|"

    for i in range(N):
        for j in range(M):
            S[i * 2 + 1][j * 2 + 1] = "o"
    
    for i in range(N - 1):
        for j in range(M):
            if abs(G[i + 1][j] - G[i][j]) == 1:
                S[i * 2 + 2][j * 2 + 1] = "."
            else:
                S[i * 2 + 2][j * 2 + 1] = "-"
    
    # スタートとゴール
    S[0][2*M - 1] = "S"
    S[2*N][2*M - 1] = "G"
    
    ans = ["".join(i) for i in S]
    print("Yes")
    for i in ans:
        print(i)


if __name__ == "__main__":
    main()