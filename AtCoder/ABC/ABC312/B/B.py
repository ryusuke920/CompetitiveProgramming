'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc312/tasks/abc312_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc312/tasks/abc312_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = []

    for i in range(n):
        for j in range(m):
            check = True
            if not (i + 8 <= n - 1 and j + 8 <= m - 1):
                check = False
                break
            for ii in range(i, i + 3):
                for jj in range(j, j + 3):
                    if s[ii][jj] == ".":
                        check = False

            for ii in range(i + 6, i + 9):
                for jj in range(j + 6, j + 9):
                    if s[ii][jj] == ".":
                        check = False

            if s[i + 3][j] == "#": check = False
            if s[i + 3][j + 1] == "#": check = False
            if s[i + 3][j + 2] == "#": check = False
            if s[i][j + 3] == "#": check = False
            if s[i + 1][j + 3] == "#": check = False
            if s[i + 2][j + 3] == "#": check = False
            if s[i + 3][j + 3] == "#": check = False
            if s[i + 5][j + 5] == "#": check = False
            if s[i + 5][j + 6] == "#": check = False
            if s[i + 5][j + 7] == "#": check = False
            if s[i + 5][j + 8] == "#": check = False
            if s[i + 6][j + 5] == "#": check = False
            if s[i + 7][j + 5] == "#": check = False
            if s[i + 8][j + 5] == "#": check = False

            if check:
                ans.append((i + 1, j + 1))

    for i, j in ans:
        print(i, j)


if __name__ == "__main__":
    main()