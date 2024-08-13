'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc351/tasks/abc351_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc351/tasks/abc351_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] != b[i][j]:
                exit(print(i + 1, j + 1))

if __name__ == "__main__":
    main()