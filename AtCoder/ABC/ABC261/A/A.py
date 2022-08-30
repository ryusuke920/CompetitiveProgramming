'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc261/tasks/abc261_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc261/tasks/abc261_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    l1, r1, l2, r2 = map(int, input().split())

    if l1 >= r2 or l2 >= r1:
        exit(print(0))

    if l1 <= l2:
        print(min(r1 - l2, r2 - l2))
    else:
        print(min(r1 - l1, r2 - l1))

if __name__ == "__main__":
    main()