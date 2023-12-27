'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc329/tasks/abc329_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc329/tasks/abc329_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in a:
        if i != a[0]:
            exit(print(i))

if __name__ == "__main__":
    main()