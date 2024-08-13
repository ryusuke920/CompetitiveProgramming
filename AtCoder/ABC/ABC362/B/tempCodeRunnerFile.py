'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc362/tasks/abc362_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc362/tasks/abc362_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())

    AB = (xa - xb)**2 + (ya - yb)**2
    BC = (xb - xc)**2 + (yb - yc)**2
    CA = (xc - xa)**2 + (yc - ya)**2

    if (AB + BC == CA) or (BC + CA == AB) or (CA + AB == BC):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()