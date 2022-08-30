from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [-1] * n


    def leader(self, a):
        while self.p[a] >= 0:
            a = self.p[a]
        return a


    def merge(self, a, b):
        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if self.p[x] > self.p[y]:
            x, y = y, x

        self.p[x] += self.p[y]
        self.p[y] = x

        return x


    def same(self, a, b):
        return self.leader(a) == self.leader(b)


    def size(self, a):
        return -self.p[self.leader(a)]


def move(prev_y: int, prev_x: int, next_y: int, next_x: int) -> None:
    grid[prev_y][prev_x], grid[next_y][next_x] = grid[next_y][next_x], grid[prev_y][prev_x]

    move_list.append((prev_y, prev_x, next_y, next_x))


def connect(yi: int, xi: int, yj: int, xj: int, mark: int) -> None:
    
    connect_list.append((yi, xi, yj, xj))

    if mark == 0: # 横に線を引いていく
        for j in range(xi, xj):
            w_ok_line[yi][j] = False

    if mark == 1: # 縦に線を引いていく
        for i in range(yi, yj):
            h_ok_line[i][xi] = False


def judge(start: int, end: int, const: int, mark: int) -> bool:

    is_ok = True
    obstacle = True

    if mark == 0: # 横を探索 <=> y 座標が const となる
        for j in range(start, end):
            is_ok &= w_ok_line[const][j]

            if w_ok_line[const][j] and j != start:
                obstacle = False
                break

    if mark == 1: # 縦を探索 <=> x 座標が const となる
        for i in range(start, end):
            is_ok &= h_ok_line[i][const]

            if h_ok_line[i][const] and i != start:
                obstacle = False
                break

    return is_ok & obstacle


def output() -> None:
    print(len(move_list))
    for yi, xi, yj, xj in move_list:
        print(yi, xi, yj, xj)

    print(len(connect_list))
    for yi, xi, yj, xj in connect_list:
        print(yi, xi, yj, xj)


def main() -> None:

    global grid, move_list, connect_list, h_ok_line, w_ok_line

    n, k = map(int, input().split())
    grid = [list(map(int, list(input()))) for _ in range(n)]

    num = 0 # 移動 + 接続回数
    move_list, connect_list = [], [] # 移動の出力配列, 接続の出力配列
    h_ok_line = [[True] * n for _ in range(n)] # 縦の接続可能確認用配列
    w_ok_line = [[True] * n for _ in range(n)] # 横の接続可能確認用配列
    INF = float('inf')

    d = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                d[grid[i][j]].append([i, j])

    for i in range(k):
        # y でソート <=> x が近いかどうかをみていく <=> 横に探索
        d[i + 1].sort(key=lambda x: x[0])

        l = len(d[i + 1])
        for j in range(l - 1):
            yi, xi = d[i + 1][j]
            yj, xj = d[i + 1][j + 1]
            
            # 同じ列じゃない場合除外
            if yi != yj:
                continue

            # 距離が近いものを繋いでいきたいので距離があるもの同士は接続可能であっても除外
            dist = abs(xi - xj)
            if dist > 30:
                continue

            # 接続どうかを判定する (0: 横, 1: 縦）
            if not judge(xi, xj, yi, 0):
                continue

            # 接続する
            connect(yi, xi, yj, xj, 0)
            num += 1

            if num == 100:
                output()
                exit()

        # x でソート <=> y が近いかどうかをみていく <=> 縦に探索
        d[i + 1].sort(key=lambda x: x[1])

        l = len(d[i + 1])
        for j in range(l - 1):
            yi, xi = d[i + 1][j]
            yj, xj = d[i + 1][j + 1]
            
            # 同じ列じゃない場合除外
            if xi != xj:
                continue

            # 距離が近いものを繋いでいきたいので距離があるもの同士は接続可能であっても除外
            dist = abs(yi - yj)
            if dist > INF:
                continue

            # 接続どうかを判定する (0: 横, 1: 縦）
            if not judge(yi, yj, xi, 1):
                continue

            # 接続する
            connect(yi, xi, yj, xj, 1)
            num += 1

            if num == 100 * k:
                output()
                exit()

    output()


if __name__ == '__main__':
    main()