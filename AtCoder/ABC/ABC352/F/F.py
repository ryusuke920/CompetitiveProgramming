'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc352/tasks/abc352_f
oj t -c "python3 F.py"
oj s https://atcoder.jp/contests/abc352/tasks/abc352_f F.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from collections import deque

def f(x: int, index: int) -> tuple:
    global dist, INF, N
    res = []
    bit = 0
    for i in range(N):
        if dist[x][i] == INF:
            continue
        if index + dist[x][i] >= N or index + dist[x][i] < 0:
            return 0, []
        bit |= 1 << (index + dist[x][i])
        res.append(i)

    return bit, res


def g(x: int, index: int) -> bool:
    global N

    dp = [0]*(1 << N)
    s = set()
    for i in range(N):
        s.add(i)
    q = deque()
    bit, v = f(x, index)
    if bit == 0:
        return False
    dp[bit] = 1
    for i in v:
        s.remove(i)
    q.append(bit)

    for i in range(N):
        if i in s:
            continue
        nxt = deque()
        while q:
            bit = q.popleft()
            for j in range(N):
                nbit, v = f(i, j)
                if nbit == 0:
                    continue
                if bit & nbit:
                    continue
                nbit |= bit
                if dp[nbit] == 0:
                    dp[nbit] = 1
                    for k in v:
                        if k in s:
                            s.remove(k)
                        nxt.append(nbit)
        q = nxt
    
    return dp[(1 << N) - 1]


def main() -> None:
    global N, M, A, B, C, dist, INF
    N, M = map(int, input().split())
    A, B, C = [0]*M, [0]*M, [0]*M
    INF = 10**18
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    
    dist = [[INF]*N for _ in range(N)]
    # dist[i][j] := (i, j) の差（+- あり）
    for i in range(N):
        dist[i][i] = 0
    
    for i in range(M):
        dist[A[i]][B[i]] = -C[i]
        dist[B[i]][A[i]] = C[i]
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] == INF or dist[k][j] == INF:
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for i in range(N):
        ans = -2
        for j in range(N):
            if g(i, j):
                if ans != -2:
                    ans = -1
                    break
                ans = j
        if ans == -2:
            print(1, end=" ")
        elif ans >= 0:
            ans += 1
            print(ans, end=" ")
    


if __name__ == "__main__":
    main()