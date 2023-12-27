'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc307/tasks/abc307_g
oj t -c "python3 G.py"
oj s https://atcoder.jp/contests/abc307/tasks/abc307_g G.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n - 1):
        a[i + 1] += a[i]

    if a[n - 1] >= 0:
        d = a[n - 1] // n
        r = a[n - 1] % n
    else:
        r = (n - (-a[n - 1]) % n) % n
        d = (a[n - 1] - r) // n

    dp1 = [0] * n
    dp2 = [0] * n

    for i in range(n):
        dp2[0] = dp1[0] + abs(d * (i + 1) - a[i])
        min_ = min(i, r)
        for j in range(min_):
            dp2[j + 1] = min(dp1[j], dp1[j + 1]) + abs(d * (i + 1) + j + 1 - a[i])
        if i + 1 <= r:
            dp2[i + 1] = dp1[i] + abs((d + 1) * (i + 1) - a[i])
        for j in range(min(r, i + 1) + 1):
            dp1[j] = dp2[j]


    print(dp1[r])


if __name__ == '__main__':
    main()
