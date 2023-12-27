'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc330/tasks/abc330_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc330/tasks/abc330_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    d = int(input())

    ans = 10**18
    for x in range(int(d**0.5) + 1):
        k = x ** 2 - d
        # |k + y**2|
        if k >= 1:
            ans = min(ans, k)
        else:
            y = int((-k)**0.5)
            for i in range(-10, 10):
                ans = min(ans, abs(k + (y + i)**2))
    print(ans)


if __name__ == "__main__":
    main()