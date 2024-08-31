'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc327/tasks/abc327_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc327/tasks/abc327_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    b = int(input())
    a = 1
    while a * a < 10**18:
        if a * a == b:
            exit(print(a))
        a += 1
    print(-1)

if __name__ == "__main__":
    main()