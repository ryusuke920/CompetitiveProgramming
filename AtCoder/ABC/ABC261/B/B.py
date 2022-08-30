'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc261/tasks/abc261_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc261/tasks/abc261_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                if a[i][j] != "-":
                    exit(print("incorrect"))
            else:
                if a[i][j]!="W" and a[j][i] == "L":
                    exit(print("incorrect"))
                if a[i][j]!="L" and a[j][i] == "W":
                    exit(print("incorrect"))
                if a[i][j]!="D" and a[j][i] == "D":
                    exit(print("incorrect"))
    print("correct")

if __name__ == "__main__":
    main()