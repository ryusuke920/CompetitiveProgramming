'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc265/tasks/abc265_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc265/tasks/abc265_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, m, T = map(int, input().split())
    a = list(map(int, input().split()))
    t = [list(map(int, input().split())) for _ in range(m)]
    now = 0
    ans = T
    bool = True
    for i in range(1, n):
        ans -= a[i - 1]
        if ans <= 0:
            bool = False
        if now < m:
            if i + 1 == t[now][0]:
                ans += t[now][1]
                now += 1

    print('Yes') if bool else print('No')

if __name__ == "__main__":
    main()