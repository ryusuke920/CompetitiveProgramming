'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc367/tasks/abc367_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc367/tasks/abc367_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    s, t = input().split(".")
    t = t.rstrip("0")
    if len(t) == 0:
        print(s)
    else:
        print(s + "." + t)


if __name__ == "__main__":
    main()