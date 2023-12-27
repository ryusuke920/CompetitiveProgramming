'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc318/tasks/abc318_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc318/tasks/abc318_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    grid = [[False] * 110 for _ in range(110)]

    for i in range(n):
        a, b, c, d = map(int, input().split())
        for x in range(a, b + 1):
            for y in range(c, d + 1):
                grid[x][y] = True

    ans = 0
    for i in range(110):
        for j in range(110):
            ans += grid[i][j]
    
    print(ans)


if __name__ == "__main__":
    main()