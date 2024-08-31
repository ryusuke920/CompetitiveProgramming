'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc369/tasks/abc369_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc369/tasks/abc369_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    A, B = map(int, input().split())
    if A == B:
        print(1)
    else:
        if (A + B) % 2 == 0:
            print(3)
        else:
            print(2)


if __name__ == "__main__":
    main()