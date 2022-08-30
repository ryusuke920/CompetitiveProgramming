'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc265/tasks/abc265_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc265/tasks/abc265_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def check(y: int, x: int):
    global h, w
    if (0 <= x < w and 0 <= y < h):
        return True
    else:
        return False

def main() -> None:
    global h, w
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    num = [[0] * w for _ in range(h)]
    y, x = 0, 0
    num[0][0] = 1
    while True:
        if grid[y][x] == 'R':
            x += 1
            if not check(y, x):
                exit(print(y + 1, x))
            num[y][x] += 1
        if grid[y][x] == 'L':
            x -= 1
            if not check(y, x):
                exit(print(y + 1, x + 2))
            num[y][x] += 1
        if grid[y][x] == 'U':
            y -= 1
            if not check(y, x):
                exit(print(y + 2, x + 1))
            num[y][x] += 1
        if grid[y][x] == 'D':
            y += 1
            if not check(y, x):
                exit(print(y, x + 1))
            num[y][x] += 1
        
        if num[y][x] >= 2:
            exit(print(-1))

if __name__ == "__main__":
    main()