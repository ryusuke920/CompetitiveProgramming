'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc305/tasks/abc305_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc305/tasks/abc305_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    p, q = input().split()
    s = "A__BC___DE____F________G"
    print(abs(s.index(p) - s.index(q)))


if __name__ == "__main__":
    main()