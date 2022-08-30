'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/ahc013/tasks/ahc013_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/ahc013/tasks/ahc013_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from collections import defaultdict

import sys
debug = lambda *x: print(*x, file = sys.stderr)


def initialize() -> None:
    """initialize"""

    global grid, move_list, connect_list, can_move, h_line, w_line, num, INF, n, k, d

    n, k = map(int, input().split())
    grid = [list(map(int, list(input()))) for _ in range(n)]

    num = 0 # 移動 + 接続回数 (100 * k 超えたら exit(output()))
    move_list, connect_list = [], set() # 移動の出力配列, 接続の出力配列
    can_move = [[False] * n for _ in range(n)] # (i, j) を動かすことが可能確認用配列
    h_line = [[True] * n for _ in range(n)] # (i, j) と (i + 1, j) を繋ぐ 下の接続可能確認用配列
    w_line = [[True] * n for _ in range(n)] # (i, j) と (i, j + 1) を繋ぐ 右の接続可能確認用配列
    INF = float('inf')

    d = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                d[grid[i][j]].append((i, j))
                can_move[i][j] = True


def init_move() -> None:

    global num

    for i in range(n): # 探索する列
        cnt = [0] * 5 # i 列にそれぞれの種類のコンピュータが何個ずつあるか
        for j in range(n): # 探索する列を一つずつなめていく
            if grid[i][j]:
                cnt[grid[i][j] - 1] += 1
        
        max_num = cnt.index(max(cnt)) + 1
        for dy in range(-1, 2, 2):
            for j in range(n): # 探索する前後の列
                y = dy + i
                if 0 <= y < n:
                    if grid[y][j] == max_num and grid[i][j] == 0:
                        if num != 100 * k:
                            move(y, j, i, j)


def move(prev_y: int, prev_x: int, next_y: int, next_x: int) -> None:
    
    global num

    num += 1
    cluster = grid[prev_y][prev_x]
    d[cluster].remove((prev_y, prev_x))
    d[cluster].append((next_y, next_x))
    can_move[prev_y][prev_x] = False
    can_move[next_y][next_x] = True

    grid[prev_y][prev_x], grid[next_y][next_x] = grid[next_y][next_x], grid[prev_y][prev_x]
    move_list.append((prev_y, prev_x, next_y, next_x))


def search() -> None:
    for cluster in range(k):
        l = len(d[cluster + 1])

        # x でソート
        d[cluster + 1].sort(key=lambda x: (x[0], x[1]))
        for j in range(l - 1):
            yi, xi = d[cluster + 1][j]
            yj, xj = d[cluster + 1][j + 1]
            is_ok = True
            obstacle = True
            if yi == yj and abs(xi - xj) <= 10:
                tate = True
                for dx in range(xi, xj):
                    is_ok |= w_line[yi][dx]
                    if dx != xi and grid[yi][dx]:
                        obstacle = False
                    if dx != xi:
                        tate &= (h_line[yi - 1][dx] and h_line[yi][dx])
                is_ok &= tate
            else:
                is_ok = False
            
            if is_ok and obstacle:
                connect(yi, xi, yj, xj)
        
        # y でソート
        d[cluster + 1].sort(key=lambda x: (x[1], x[0]))
        for j in range(l - 1):
            yi, xi = d[cluster + 1][j]
            yj, xj = d[cluster + 1][j + 1]
            is_ok = True
            obstacle = True
            if xi == xj and abs(yi - yj) <= 10:
                yoko = True
                for dy in range(yi, yj):
                    is_ok |= h_line[dy][xi]
                    if dy != yi and grid[dy][xi]:
                        obstacle = False
                    if dy != yi:
                        yoko &= (w_line[dy][xi - 1] and w_line[dx][xi])
                is_ok &= yoko
            else:
                is_ok = False
        
            if is_ok and obstacle:
                connect(yi, xi, yj, xj)
        

def connect(yi: int, xi: int, yj: int, xj: int) -> None:
    
    global num

    if num != 100 * k:
        can_move[yi][xi] = False
        can_move[yj][xj] = False
        if (yi, xi, yj, xj) not in connect_list:
            connect_list.add((yi, xi, yj, xj))
            num += 1
            if yi == yj:
                for dx in range(xi, xj):
                    w_line[yi][dx] = False
            if xi == xj:
                for dy in range(yi, yj):
                    h_line[dy][xi] = False


def output() -> None:
    """出力"""
    print(len(move_list))
    for yi, xi, yj, xj in move_list:
        print(yi, xi, yj, xj)

    print(len(connect_list))
    for yi, xi, yj, xj in list(connect_list):
        print(yi, xi, yj, xj)
    debug('----最終的な移動・接続回数----')
    debug("移動回数：", len(move_list))
    debug("接続回数：", len(connect_list))
    debug("合計回数：", num)

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
    init_move()
    search()
    output()


if __name__ == '__main__':
    main()