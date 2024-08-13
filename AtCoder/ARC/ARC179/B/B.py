'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/arc179/tasks/arc179_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/arc179/tasks/arc179_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    M, N = map(int, input().split())
    X = list(map(lambda x: int(x) - 1, input().split()))
    mod = 998244353
    dp = [[0]*1100 for _ in range(N + 1)]
    dp[0][0] = 1
    num = [(1 << M) - 1]*10
    for i in range(M):
        num[X[i]] -= (1 << i)
    
    for i in range(N):
        for S in range(1 << M):
            for j in range(M):
                if (1 << j) & S:
                    continue
                nxt = S | (1 << j)
                nxt &= num[j]
                dp[i + 1][nxt] = dp[i + 1][nxt] + dp[i][S]
                dp[i + 1][nxt] %= mod
    
    ans = 0
    for i in range(1 << M):
        ans += dp[N][i]
        ans %= mod
    print(ans)
    

if __name__ == "__main__":
    main()