'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc265/tasks/abc265_e
oj t -c "python3 E.py"
oj s https://atcoder.jp/contests/abc265/tasks/abc265_e E.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline


def main() -> None:

    n, m = map(int, input().split())
    a, b, c, d, e, f = map(int, input().split())

    p = set()
    for _ in range(m):
        x, y = map(int, input().split())
        p.add((x, y))

    mod = 998244353

    if m == 0:
        exit(print(pow(3, n, mod)))

    from collections import defaultdict
    out = []
    INF = float('inf')
    b1, b2, b3 = INF, INF, INF
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                if not (1 <= i + j + k <= n):
                    continue

                x = a * i + c * j + e * k
                y = b * i + d * j + f * k
                if (x, y) in p:
                    b1, b2, b3 = i, j, k
                    #b1 = min(b1, i)
                    #b2 = min(b2, j)
                    #b3 = min(b3, k)
                    out.append(i + j + k)
        
    num = 0
    out.sort()
    for i in out[:3]:
        num += 3 ** (n - i)
    ans = 3 ** n
   # print(out)

    u = ans - num
    print(u % mod)


if __name__ == "__main__":
    main()