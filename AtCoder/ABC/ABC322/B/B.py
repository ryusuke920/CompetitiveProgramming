'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc322/tasks/abc322_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc322/tasks/abc322_b B.py --guess-python-interflag1ter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    n, m = map(int, input().split())
    s = input()
    t = input()

    flag1 = False
    flag2 = False
    if len(s) > len(t):
        exit(print(3))

    flag1 = t[: n] == s
    flag2 = t[m - n : m] == s
    if flag1 and flag2:
        print(0)
    elif flag1:
        print(1)
    elif flag2:
        print(2)
    else:
        print(3)


if __name__ == "__main__":
    main()