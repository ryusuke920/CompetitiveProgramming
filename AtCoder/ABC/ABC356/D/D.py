'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc356/tasks/abc356_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc356/tasks/abc356_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N, M = map(int, input().split())
    mod = 998244353
    ans = 0
    for i in range(61):
        if (M & (1 << i)):
            num1 = ((N + 1) // (2**(i + 1)))*((2**(i + 1)) // 2)
            num2 = (N + 1) % (2**(i + 1))
            num2 = max(0, num2 - ((2**(i + 1)) // 2))
            num1 += num2
            ans += num1
            ans %= mod

    print(ans)


if __name__ == "__main__":
    main()