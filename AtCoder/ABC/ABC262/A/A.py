'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc262/tasks/abc262_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc262/tasks/abc262_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    while True:
        if n % 4 == 2:
            exit(print(n))
        n += 1

if __name__ == "__main__":
    main()