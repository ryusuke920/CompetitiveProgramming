'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc263/tasks/abc263_a
oj t -c "python3 a.py"
oj s https://atcoder.jp/contests/abc263/tasks/abc263_a a.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    a = sorted(list(map(int, input().split())))

    if len(set(a)) == 1:
        exit(print("No"))

    if a[0] == a[1] == a[2] and a[3] == a[4]:
        exit(print("Yes"))

    if a[0] == a[1] and a[2] == a[3] == a[4]:
        exit(print("Yes"))

    print("No")

if __name__ == "__main__":
    main()