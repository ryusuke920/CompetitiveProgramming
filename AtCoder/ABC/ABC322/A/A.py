'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc322/tasks/abc322_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc322/tasks/abc322_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    n = int(input())
    s = input()
    for i in range(n - 2):
        if s[i : i + 3] == "ABC":
            exit(print(i + 1))
    
    print(-1)


if __name__ == "__main__":
    main()