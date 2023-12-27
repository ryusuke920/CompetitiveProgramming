'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc285/tasks/abc285_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc285/tasks/abc285_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    n = int(input())
    s = input()
    for i in range(1, n):
        for j in range(1, n + 1):
            if i + j > n:
                print(j - 1)
                break
            if s[j - 1] == s[i + j - 1]:
                print(j - 1)
                break


if __name__ == "__main__":
    main()