'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc341/tasks/abc341_f
oj t -c "python3 F.py"
oj s https://atcoder.jp/contests/abc341/tasks/abc341_f F.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    x = 3
    print(~x, not x, not 0, not 1)

if __name__ == "__main__":
    main()