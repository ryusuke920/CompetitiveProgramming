'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc309/tasks/abc309_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc309/tasks/abc309_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    n = int(input())
    a = [list(map(int, list(input()))) for _ in range(n)]
    #print(*a)
    b = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[i][j] = a[i][j]
    
    for i in range(n - 1):
        b[0][i + 1] = a[0][i]
    b[0][0] = a[1][0]
    for i in range(n - 1):
        b[i + 1][n - 1] = a[i][n - 1]
    b[0][n - 1] = a[0][n - 2]
    for i in range(n - 1):
        b[n - 1][i] = a[n - 1][i + 1]
    b[n - 1][n - 1] = a[n - 2][n - 1]
    for i in range(n - 1):
        b[i][0] = a[i + 1][0]
    b[n - 1][0] = a[n - 1][1]
    for i in range(n):
        print(*b[i], sep="")

if __name__ == "__main__":
    main()