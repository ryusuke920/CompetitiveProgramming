'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc262/tasks/abc262_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc262/tasks/abc262_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
# dp[i][j] := [i, j)までみた時の平均値が整数であるものの個数

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    # dp[l][r]の合計 := [l, r) := s[r] - s[l - 1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for w in range(n):
        dp[w][w + 1] = 1
    
    for w in range(2, n + 1):
        for l in range(n - w + 1):
            r = l + w
            print(l,r,w)
            cnt = -10 ** 18
            for i in range(l + 1, r):
                print('span=',l,i,r)
                cnt = max(cnt, dp[l][i] + dp[l + 1][r])
            
            dp[l][r] += cnt
            if (s[r] - s[l]) % w == 0:
                dp[l][r] += 1

            dp[l][r] %= mod

            print(*dp, sep='\n')
            print()

    
    print(*dp, sep='\n')
    print(dp[0][n])

if __name__ == "__main__":
    main()