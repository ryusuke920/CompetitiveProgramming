'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc346/tasks/abc346_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc346/tasks/abc346_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n - 1):
        b.append(a[i] * a[i + 1])
    print(*b)

if __name__ == "__main__":
    main()