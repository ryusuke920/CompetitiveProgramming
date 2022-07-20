'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc374/tasks/abc374_g
oj t -c "python3 G.py"
oj s https://atcoder.jp/contests/abc374/tasks/abc374_g G.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    pass

if __name__ == "__main__":
    main()