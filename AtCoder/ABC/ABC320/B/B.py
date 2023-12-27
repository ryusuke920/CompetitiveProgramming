'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc320/tasks/abc320_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc320/tasks/abc320_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


def main() -> None:
    s = input()
    l = len(s)
    ans = 0
    for i in range(l):
        for j in range(l):
            if i > j:
                continue
            t = s[i:j + 1]
            if t == t[::-1]:
                ans = max(ans, j - i + 1)
    
    print(ans)


if __name__ == "__main__":
    main()