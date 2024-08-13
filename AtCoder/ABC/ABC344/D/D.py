'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc344/tasks/abc344_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc344/tasks/abc344_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

def main() -> None:
    t = input()
    len_ = len(t)
    n = int(input())
    a = []
    b = []
    for i in range(n):
        _, *s = list(input().split())
        a.append(s)
        b.append(_)
    print(*a,sep="\n")
    INF = 10**18
    # dp[i][j] := i 番目までの袋で先頭から j 文字を一致させることができる時の最小値
    dp = [[INF] * (len_ + 1) for _ in range(n + 1)]
    dp[0][0] = 0


if __name__ == "__main__":
    main()