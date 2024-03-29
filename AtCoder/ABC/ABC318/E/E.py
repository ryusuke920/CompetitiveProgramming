'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc318/tasks/abc318_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc318/tasks/abc318_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

'''
a = b = c
a = b != c
a != b = c
a != b != c
'''

import sys
input = sys.stdin.readline

def main() -> None:
    pass

if __name__ == "__main__":
    main()