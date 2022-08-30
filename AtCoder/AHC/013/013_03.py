from collections import defaultdict

import sys
debug = lambda *x: print(*x, file = sys.stderr)


def initialize() -> None:
    """initialize"""

    global grid, move_list, connect_list, h_ok_line, w_ok_line, num, INF, n, k, d

    n, k = map(int, input().split())
    grid = [list(map(int, list(input()))) for _ in range(n)]

    num = 0 # 移動 + 接続回数 (100 * k 超えたら exit())
    move_list, connect_list = [], [] # 移動の出力配列, 接続の出力配列
    h_ok_line = [[True] * n for _ in range(n)] # 縦の接続可能確認用配列
    w_ok_line = [[True] * n for _ in range(n)] # 横の接続可能確認用配列
    INF = float('inf')

    d = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                d[grid[i][j]].append((i, j))


def move(prev_y: int, prev_x: int, next_y: int, next_x: int, cluster: int) -> None:
    """移動"""
    '''
    debug('koko')
    debug(d)
    debug(prev_y, prev_x, next_y, next_x)
    for i in h_ok_line:
        debug(i)
    debug()
    for i in w_ok_line:
        debug(i)
    debug()
    '''


    grid[prev_y][prev_x], grid[next_y][next_x] = grid[next_y][next_x], grid[prev_y][prev_x]
    d[cluster].remove((prev_y, prev_x))
    d[cluster].append((next_y, next_x))

    move_list.append((prev_y, prev_x, next_y, next_x))


def can_move() -> None:

    global num

    for i in range(k):

        l = len(d[i + 1])

        for j in range(l):
            for kk in range(l):
                if j == kk:
                    continue

                yi, xi = d[i + 1][j]
                yj, xj = d[i + 1][kk]

                # マンハッタン距離が 5 以内でない場合は continue
                dist = abs(xi - xj) + abs(yi - yj)
                if dist > 10:
                    continue
                
                if num + dist + 1 > 100 * k:
                    continue

                check_move = False

                # yi に合わせる場合 <=> (yj, xj) を動かす
                if (h_ok_line[yj][xj] and w_ok_line[yj][xj]):
                    # 便宜上 xi < xj & yi < yj
                    if (xi < xj and yi < yj):
                        check_move = True
                        for ii in range(yi, yj + 1):
                            check_move &= h_ok_line[ii][xj]
                        for jj in range(xi, xj + 1):
                            check_move &= w_ok_line[yi][jj]

                if check_move:
                    move(yj, xj, yi, xj, i + 1)
                    num += dist
                    connect(yi, xi, yi, xj, 0)
                    num += 1
                    return


def connect(yi: int, xi: int, yj: int, xj: int, mark: int) -> None:
    """接続"""

    connect_list.append((yi, xi, yj, xj))

    if mark == 0: # 横に線を引いていく
        for j in range(xi, xj + 1):
            w_ok_line[yi][j] = False

    if mark == 1: # 縦に線を引いていく
        for i in range(yi, yj + 1):
            h_ok_line[i][xi] = False


def judge(start: int, end: int, const: int, mark: int) -> bool:
    """接続可能か調べる"""

    is_ok = True
    obstacle = True

    #debug('各値:', start,end, const, mark)

    if mark == 0: # 横を探索 <=> y 座標が const となる
        for j in range(start, end + 1):
            if j != start and j != end:
                is_ok &= w_ok_line[const][j]
                is_ok &= h_ok_line[const][j]

            if (grid[const][j]) and (j != start and j != end):
                obstacle = False
                break

    if mark == 1: # 縦を探索 <=> x 座標が const となる
        for i in range(start, end + 1):
            if i != start and i != end:
                is_ok &= h_ok_line[i][const]
                is_ok &= w_ok_line[i][const]

            if (grid[i][const]) and (i != start and i != end):
                obstacle = False
                break

    return is_ok and obstacle


def search() -> None:
    """ループ"""

    global num

    for i in range(k):
        # y でソート <=> x が近いかどうかをみていく <=> 横に探索
        d[i + 1].sort(key=lambda x: x[0])

        l = len(d[i + 1])
        for j in range(l - 1):
            yi, xi = d[i + 1][j]
            yj, xj = d[i + 1][j + 1]
            
            # 同じ列じゃない場合除外
            if yi == yj:
                # 距離が近いものを繋いでいきたいので距離があるもの同士は接続可能であっても除外
                dist = abs(xi - xj)
                if dist <= 15:
                    # 接続どうかを判定する (0: 横, 1: 縦）
                    if judge(xi, xj, yi, 0):
                        if num + 1 <= 100 * k:
                            # 接続する
                            connect(yi, xi, yj, xj, 0)
                            num += 1
                            if num == 100 * k:
                                output()
                                exit()


        # x でソート <=> y が近いかどうかをみていく <=> 縦に探索
        d[i + 1].sort(key=lambda x: x[1])

        l = len(d[i + 1])
        for j in range(l - 1):
            yi, xi = d[i + 1][j]
            yj, xj = d[i + 1][j + 1]
            
            # 同じ列じゃない場合除外
            if xi == xj:
                # 距離が近いものを繋いでいきたいので距離があるもの同士は接続可能であっても除外
                dist = abs(yi - yj)
                if dist <= INF:
                    # 接続どうかを判定する (0: 横, 1: 縦）
                    if judge(yi, yj, xi, 1):
                        if num + 1 <= 100 * k:
                            # 接続する
                            connect(yi, xi, yj, xj, 1)
                            num += 1
                            if num == 100 * k:
                                output()
                                exit()


def output() -> None:
    """出力"""
    print(len(move_list))
    for yi, xi, yj, xj in move_list:
        print(yi, xi, yj, xj)

    print(len(connect_list))
    for yi, xi, yj, xj in connect_list:
        print(yi, xi, yj, xj)
    '''
    debug('最終的なconnect')
    for i in h_ok_line:
        debug(i)
    debug()
    for i in w_ok_line:
        debug(i)
    debug()
    '''


def main() -> None:
    initialize()

    search()
    #can_move()

    output()


if __name__ == '__main__':
    main()