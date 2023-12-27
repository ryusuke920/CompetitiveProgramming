'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc326/tasks/abc326_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc326/tasks/abc326_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    x, y = map(int, input().split())
    if x - y == 3 or x - y == 2 or x - y == 1 or x - y == 0 or x - y == -1 or x - y == -2:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()