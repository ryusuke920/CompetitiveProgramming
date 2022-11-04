'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc263/tasks/abc263_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc263/tasks/abc263_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline


def main() -> None:
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))

    sum_a, sum_b, max_b = 0, 0, 0
    ans = r * n
    for i in range(n):
        sum_a += a[i]
        sum_b += a[i] - l
        max_b = max(max_b, sum_b)
        now = sum_a + r * (n - i - 1) - max_b
        ans = min(ans, now)
    
    print(ans)


if __name__ == "__main__":
    main()