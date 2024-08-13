# テーマ: 大クレーンのみを使って全部のコンテナを運ぶ

import sys
input = sys.stdin.readline
from collections import deque

def debug(*args, end="\n"):
    print(*args, end=end, file=sys.stderr)


def init() -> None:
    for i in range(N):
        crane.append((i, 0))


def is_want() -> list:
    """今運搬したいコンテナの index を返す O(N^2)"""
    want = []
    for i in range(N):
        now = -1
        for j in range(N):
            if is_done[i*N + j]:
                continue
            now = i*N + j
        if now != -1:
            want.append(now)
    
    return want


def is_near(sy: int, sx: int) -> tuple:
    """今 (sy, sx) にいる時の今欲しいコンテナの座標 (gy, gx) を返す"""
    want = is_want()
    len_ = len(want)
    near = []
    for i in range(N):
        for j in range(N):
            for k in range(len_):
                if grid[i][j] == want[k]:
                    cost = abs(sy - i) + abs(sx - j)
                    near.append((want[k], i, j, cost))
    
    if len(near) >= 1:
        near.sort(key=lambda x: x[3])
        return (near[0][1], near[0][2])
    else:
        return (-1, -1)


def to_put(ind: int, sy: int, sx: int, gy: int, gx: int) -> tuple:
    """
        クレーン ind を (sy, sx) から (gy, gx) へ移動し、
        そこにあるコンテナを掴み、
        排出口 (exit_y, exit_x) へと運ぶ、
        返り値は運んだ後の排出口の座標 (exit_y, exit_x)
    """

    # x 方向の移動
    if sx < gx: S[ind].append("R"*(gx - sx))
    else: S[ind].append("L"*(sx - gx))

    # y 方向の移動
    if sy < gy: S[ind].append("D"*(gy - sy))
    else: S[ind].append("U"*(sy - gy))

    # コンテナを掴む
    S[ind].append("P")
    
    # コンテナの番号
    container_num = grid[gy][gx]

    # どの排出口が正しいかを見つける
    exit_y, exit_x = container_num // N, N - 1

    # y 方向の移動（x から行くと先に出口に行ってしまう）
    if gy < exit_y: S[ind].append("D"*(exit_y - gy))
    else: S[ind].append("U"*(gy - exit_y))

    # x 方向の移動
    S[ind].append("R"*((N - 1) - gx))

    # コンテナを排出口に下ろす
    S[ind].append("Q")

    # コンテナを grid から削除して、is_done を書き換える
    grid[gy][gx] = -1
    is_done[container_num] = True

    # コンテナが (gy, 0) にある場合は最後のコンテナを追加する
    if gx == 0 and len(q[gy]):
        grid[gy][gx] = q[gy][0]
        q[gy].popleft()

    return (exit_y, exit_x)


def debug_grid() -> None:
    """盤面の debug をする"""
    debug("↓盤面の出力↓")
    for i in range(N):
        debug(*grid[i])
    debug()


def debug_is_done() -> None:
    """is_done の debug をする"""
    debug("↓ is_done の出力 ↓")
    for i in range(N):
        debug(*is_done[i*5 : (i + 1)*5])
    debug()


def output() -> None:
    for i in range(N):
        print("".join(S[i]))


def main() -> None:
    global N, A, grid, is_done, S, crane, q
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    grid = [[-1]*N for _ in range(N)]
    is_done = [False]*(N**2) # 終わったかどうか
    crane = []
    q = [deque() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            q[i].append(A[i][j])
    
    for i in range(N):
        for j in range(N - 1):
            q[i].popleft()
    S = [[] for _ in range(N)]


    # 全部のコンテナを出す
    # PRRRRQLLLL PRRRQLLL PRRQLL PRQB
    for j in "PRRRQLLLPRRQLLPRQ":
        S[0].append(j)

    for i in range(1, N):
        for j in "PRRRQLLLPRRQLLPRQB":
            S[i].append(j)
    
    for i in range(N):
        for j in range(N - 1):
            grid[i][j] = A[i][3 - j]
    
    now_y, now_x = 0, 1
    while True:
        nxt_y, nxt_x = is_near(now_y, now_x)
        if (nxt_y, nxt_x) == (-1, -1):
            break
        now_y, now_x = to_put(0, now_y, now_x, nxt_y, nxt_x)

    # 盤面の出力
    # debug_grid()

    # is_done の出力
    # debug_is_done()

    # 答えの出力
    output()


if __name__ == "__main__":
    main()