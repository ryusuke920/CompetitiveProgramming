'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc369/tasks/abc369_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc369/tasks/abc369_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[0]*2 for _ in range(N + 1)]
    dp[0][1] = 0
    INF = 10**18
    dp[0][0] = -INF

    for i in range(N):
        dp[i + 1][0] = max(dp[i][0], dp[i][1] + A[i])
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + 2*A[i])
    
    print(max(dp[N]))


if __name__ == "__main__":
    main()