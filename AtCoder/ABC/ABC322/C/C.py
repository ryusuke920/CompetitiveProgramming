'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc322/tasks/abc322_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc322/tasks/abc322_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

from bisect import bisect_left, bisect_right

def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        t = bisect_left(a, i + 1)
        print(a[t] - (i + 1))


if __name__ == "__main__":
    main()