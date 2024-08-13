'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc365/tasks/abc365_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc365/tasks/abc365_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    Y = int(input())
    if Y % 4 != 0:
        print(365)
    elif Y % 4 == 0and Y % 100 != 0:
        print(366)
    elif Y % 100 == 0 and Y % 400 != 0:
        print(365)
    else:
        print(366)

if __name__ == "__main__":
    main()