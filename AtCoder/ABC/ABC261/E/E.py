'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc261/tasks/abc261_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc261/tasks/abc261_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, c = map(int, input().split())
    prev = c
    num = []
    for i in range(n):
        t, a = map(int, input().split())
        if t == 1:
            c &= a
        if t == 2:
            c |= a
        if t == 3:
            c ^= a
        num.append(c)
    print(num)

if __name__ == "__main__":
    main()