'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc369/tasks/abc369_f
oj t -c "python3 F.py"
oj s https://atcoder.jp/contests/abc369/tasks/abc369_f F.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    H, W, N = map(int, input().split())

if __name__ == "__main__":
    main()