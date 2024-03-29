'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc308/tasks/abc308_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc308/tasks/abc308_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    s = list(map(int, input().split()))

    for i in s:
        if i % 25 == 0 and 100 <= i <= 675:
            continue
        else:
            exit(print("No"))

    for i in range(7):
        if s[i] > s[i + 1]:
            exit(print("No"))

    print("Yes")


if __name__ == "__main__":
    main()