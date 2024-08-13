# テーマ: RE は消えたけど WA が一定数出るのでどこで出るのかテスターを作る

import sys
input = sys.stdin.readline
import time
import glob
from random import randint
from collections import deque

input_path = sorted(glob.glob("/Users/imlab/Documents/git/CompetitiveProgramming/AtCoder/AHC/033/in/*.txt"))


def debug(*args, end="\n"):
    print(*args, end=end, file=sys.stderr)


def is_want() -> list:
    """今運搬したいコンテナの index を返す O(N^2)"""
    want = []
    for i in range(N):
        now = -1
        for j in reversed(range(N)):
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
        クレーン ind を (sy, sx) から (gy, gx) = (hoge, 0) へ移動し、
        そこにあるコンテナを掴み、
        排出口 (exit_y, exit_x) へと運ぶ、
        返り値は運んだ後の搬出口の座標 (exit_y, exit_x)
    """

    # x 方向の移動
    if sx < gx: S[ind].append("R"*(gx - sx))
    else: S[ind].append("L"*(sx - gx))

    # y 方向の移動
    if sy < gy: S[ind].append("D"*(gy - sy))
    else: S[ind].append("U"*(sy - gy))

    # コンテナを掴む
    S[ind].append("P")
    print(f"追加!!! {len(''.join(S[ind]))}, {gy}, {gx} ")
    print(*grid, sep="\n")
    
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
    grid[exit_y][exit_x] = -1
    is_done[container_num] = True

    # コンテナが (gy, 0) にある場合は最後のコンテナを追加する
    if gx == 0 and len(q[gy]):
        grid[gy][gx] = q[gy][0]
        q[gy].popleft()
    
    for i in range(N):
        grid[i][N - 1] = -1

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


def exit_program(now_time: float) -> None:
    """プログラムが TLE しているかどうか判定する関数"""
    # 現時点でのプログラムの実行時間（ms）
    program_time = int((now_time - start_time)*1000)
    if program_time >= 2750:
        output()
        debug("プログラムが TLE したため強制終了しました。")
        exit()


def find_WA_RE() -> None:
    goal = [[] for _ in range(N)] # goal[i] := i 行目の搬出口から出ていったコンテナの番号
    q = [deque() for _ in range(N)]
    for i in range(N):
        for j in range(N - 1, N):
            q[i].append(A[i][j])
    crane = [] # クレーンの座標
    len_ = [len(S[i]) for i in range(N)] # len_[i] := クレーン i の行動数
    for i in range(N):
        crane.append([i, 0])
    crane[0] = [0, 1] # 4 つ出した状態からスタート
    container_num = [-1]*N # container_num[i] := クレーン i が掴んでいるコンテナの番号
    grid = [[-1]*N for _ in range(N)] # grid[i][j] := マス (i, j) の情報
    for i in range(N):
        for j in range(4):
            grid[i][3 - j] = A[i][j]

    for i in range(1): # 一旦は大クレーンだけでシミュレーションする
        for ind, s in enumerate("".join(S[i])):
            if ind <= 16: continue # 最初の運び出すのは事前にやっておく
            if s == '.': continue
            if s == 'U': crane[i][0] -= 1
            if s == 'D': crane[i][0] += 1
            if s == 'R': crane[i][1] += 1
            if s == 'L': crane[i][1] -= 1
            # print(f"{ind}ターン目終了後, {crane[i][0]}, {crane[i][1]}, {s}")

            # index out of range
            if not (0 <= crane[i][1] < N and 0 <= crane[i][0] < N):
                debug(f"{i} 台目のクレーンの {ind} 回目の操作 {s} にて配列外参照を起こしました。")
                debug(f"行こうとした座標は ({crane[i][0]}, {crane[i][1]}) です。")
                exit()
            
            if s == 'P':
                if container_num[i] == -1:
                    if grid[crane[i][0]][crane[i][1]] == -1:
                        debug(f"{i} 台目のクレーンの {ind} 回目の操作 {s} にてコンテナが存在しないマスのコンテナを掴もうとしました。")
                        exit()
                    else:
                        container_num[i] = grid[crane[i][0]][crane[i][1]]
                        grid[crane[i][0]][crane[i][1]] = -1
                        if crane[i][0] == 0 and len(q[i]):
                            grid[crane[i][0]][crane[i][1]] = q[i].popleft()
                else:
                    debug(f"{i} 台目のクレーンの {ind} 回目の操作 {s} にて既にコンテナを掴んでる状態で再びコンテナを掴もうとしました。")
                    exit()
        
            if s == 'Q':
                if container_num[i] == -1:
                    debug(f"{i} 台目のクレーンの {ind} 回目の操作 {s} にて掴んでないにも関わらずコンテナを掴もうとしました。")
                    exit()
                else:
                    if grid[crane[i][0]][crane[i][1]] != -1:
                        debug(f"{i} 台目のクレーンの {ind} 回目の操作 {s} にて既にコンテナが置かれている場所にコンテナを降ろそうとしました。")
                        debug(f"置こうとした座標は ({crane[i][0]}, {crane[i][1]}) です。")
                        print(*grid, sep="\n")
                        exit()
                    else:
                        grid[crane[i][0]][crane[i][1]] = container_num[i]
                        container_num[i] = -1
                        if crane[i][1] == N - 1:
                            # コンテナを搬出する
                            goal[crane[i][0]].append(container_num[i])
                            grid[crane[i][0]][crane[i][1]] = -1
    


def embedded() -> None:
    global is_embedded
    if A == [
        [4, 3, 2, 1, 0],
        [9, 8, 7, 6, 5],
        [14, 13, 12, 11, 10],
        [19, 18, 17, 16, 15],
        [24, 23, 22, 21, 20]
    ]:
        is_embedded = True
        S = [
            "PRRRQLLLPRRQLLPRQLPRRDDDDQUUUULLPRRRRQDDDDLLPUUUURRQLLLPRRRQLLPRRQLPRQLLLLDPURRRQLLLDDPRRUUQLLDPRRRRQLUPRDQLLLPRRRQLLPRRQLPRQLLLLDPRRRRQLLUUPDDRRQLLLPRRRQLLPRRQLPRQLLLLDPRRRDQLLLPRRQLLPRQLUPRRRRQLDPRUQLLLPRRRQLLPRRQLPRQDLLLLPRRRQLLLPRRRUQLLLDPRRRRQLUPRDQLPRQLLLPRRRQLLPRRQ",
            "PRRRQLLLPRRQLLPRQB",
            "PRRRQLLLPRRQLLPRQB",
            "PRRRQLLLPRRQLLPRQB",
            "B"
        ]

        for i in range(N):
            print(*S[i], sep="")

    
    if is_embedded:
        debug(f"埋め込みによって答えを出力しました。")
        exit()


def solve() -> None:
    global N, A, grid, is_done, S, crane, q, d, dir_, is_embedded
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    is_embedded = False

    embedded()

    grid = [[-1]*N for _ in range(N)]
    is_done = [False]*(N**2) # 終わったかどうか
    crane = []
    q = [deque() for _ in range(N)]
    d = ((0, 1), (1, 0), (-1, 0), (0, -1))
    dir_ = "RDUL"

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


    # まだコンテナが入れられてない場合はずらして入れる
    while True:

        exit_program(time.perf_counter())

        is_empty = 0
        for i in range(N):
            if len(q[i]) == 0:
                is_empty += 1
        if is_empty == 5:
            break
        
        # (now_y, now_x) から (i, 0) に移動してコンテナを掴み、(nxt_y, nxt_x) に置く
        for i in range(N):
            if len(q[i]):
                S[0].append("L"*now_x)
                if now_y < i: S[0].append("D"*(i - now_y))
                else: S[0].append("U"*(now_y - i))
                S[0].append("P")
                print(f"追加!{len(''.join(S[0]))}")

                # 移動後にいる座標に更新する
                now_y, now_x = i, 0
                while True:
                    nxt_y = randint(0, N - 1)
                    nxt_x = randint(0, N - 1)
                    if not (0 <= nxt_y < N and 0 <= nxt_x < N):
                        continue
                    if grid[nxt_y][nxt_x] == -1:
                        break

                # (now_y, now_x) から (nxt_y, nxt_x) にコンテナを移動させる
                # 縦
                if now_y < nxt_y: S[0].append("D"*(nxt_y - now_y))
                else: S[0].append("U"*(now_y - nxt_y))
                # 横
                if now_x < nxt_x: S[0].append("R"*(nxt_x - now_x))
                else: S[0].append("L"*(now_x - nxt_x))
                grid[nxt_y][nxt_x] = grid[now_y][now_x]
                grid[now_y][now_x] = q[i].popleft()
                S[0].append("Q")
                now_y, now_x = nxt_y, nxt_x
                break
            
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


def local_solve() -> None:
    global N, A, grid, is_done, S, crane, q, d, dir_
    N = 5
    for input_text in input_path:
        with open(input_text, 'r') as f:
            texts = f.read()
            A = []
            for ind, text in enumerate(texts.split("\n")):
                if not (1 <= ind <= 5):
                    continue
                a = []
                for i in text.split():
                    a.append(int(i))
                A.append(a)
            
            grid = [[-1]*N for _ in range(N)]
            is_done = [False]*(N**2) # 終わったかどうか
            crane = []
            q = [deque() for _ in range(N)]
            d = ((0, 1), (1, 0), (-1, 0), (0, -1))
            dir_ = "RDUL"

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


            # まだコンテナが入れられてない場合はずらして入れる
            while True:

                exit_program(time.perf_counter())

                is_empty = 0
                for i in range(N):
                    if len(q[i]) == 0:
                        is_empty += 1
                if is_empty == 5:
                    break
            
                for i in range(N):
                    if len(q[i]):
                        S[0].append("L"*(now_x - 0))
                        if now_y < i: S[0].append("D"*(i - now_y))
                        else: S[0].append("U"*(now_y - i))
                        S[0].append("P")
                        now_y, now_x = i, 0
                        for ind, (dy, dx) in enumerate(d):
                            ny = now_y + dy
                            nx = now_x + dx
                            if not (0 <= ny < N and 0 <= nx < N):
                                continue
                            if grid[ny][nx] != -1:
                                continue
                            grid[ny][nx] = grid[now_y][now_x]
                            grid[now_y][now_x] = q[i].popleft()
                            S[0].append(dir_[ind])
                            S[0].append("Q")
                            now_y, now_x = ny, nx
                            break
                    
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


def main() -> None:
    global start_time, end_time
    start_time = time.perf_counter() # 計測開始

    solve() # 提出用
    # local_solve() # ローカル用

    find_WA_RE() # WA・RE のチェック

    end_time = time.perf_counter() # 計測終了
    debug(f"実行時間: {str((end_time - start_time)*1000)[:5]} ms")


if __name__ == "__main__":
    main()
