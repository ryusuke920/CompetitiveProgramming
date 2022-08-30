'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc268/tasks/abc268_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc268/tasks/abc268_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    # dp[i] := i ターン目のスコアの期待値
    dp = [0] * (n + 1)
    dp[1] = 3.5
    for i in range(2, n + 1):
        num = 0
        for j in range(1, 7):
            # 終わる場合
            if dp[i - 1] < j:
                num += j
            # 続ける場合
            elif dp[i - 1] >= j:
                num += dp[i - 1]
        dp[i] = num / 6
    
    print(dp[n])

if __name__ == "__main__":
    main()