'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc361/tasks/abc361_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc361/tasks/abc361_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def f(a, b, c, d, e, f, g, h, i, j, k, l):
    x_overlap = max(0, min(d, j) - max(a, g))
    y_overlap = max(0, min(e, k) - max(b, h))
    z_overlap = max(0, min(f, l) - max(c, i))
    

    return x_overlap * y_overlap * z_overlap > 0


def main() -> None:
    a, b, c, d, e, f = map(int, input().split())
    g, h, i, j, k, l = map(int, input().split())

    if f(a, b, c, d, e, f, g, h, i ,j ,k ,l):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()