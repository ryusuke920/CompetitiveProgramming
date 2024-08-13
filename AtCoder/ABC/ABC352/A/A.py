'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc352/tasks/abc352_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc352/tasks/abc352_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N, X, Y, Z = map(int, input().split())
    if min(X, Y) <= Z <= max(X, Y):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()