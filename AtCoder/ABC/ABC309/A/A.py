'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc309/tasks/abc309_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc309/tasks/abc309_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    a, b = map(int, input().split())
    l = [[1, 2], [2, 3], [4, 5], [5, 6], [7, 8], [8, 9]]
    for i, j in l:
        if (i, j) == (a, b):
            exit(print("Yes"))
    
    print("No")


if __name__ == "__main__":
    main()