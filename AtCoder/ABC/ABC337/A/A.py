'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc337/tasks/abc337_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc337/tasks/abc337_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a, b = 0, 0
    for i in range(n):
        x, y = map(int, input().split())
        a += x
        b += y
    if a == b:
        print("Draw")
    elif a > b:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()