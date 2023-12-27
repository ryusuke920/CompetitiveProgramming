'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc311/tasks/abc311_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc311/tasks/abc311_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    n = int(input())
    s = input()
    a = [False, False, False]
    for i in range(n):
        if s[i] == "A":
            a[0] = True
        if s[i] == "B":
            a[1] = True
        if s[i] == "C":
            a[2] = True
        if a[0] and a[1] and a[2]:
            exit(print(i + 1))

if __name__ == "__main__":
    main()