'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/arc162/tasks/arc162_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/arc162/tasks/arc162_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        ans = 0
        ind = 10**18
        for i in reversed(range(n)):
            if p[i] < ind:
                ind = p[i]
                ans += 1

        print(ans)


if __name__ == "__main__":
    main()