'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc265/tasks/abc265_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc265/tasks/abc265_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    x, y, n = map(int, input().split())
    ans = []
    for i in range(10000):
        if 3 * i > n:
            continue
        if y * i + (n - 3 * i) * x > 0:
            ans.append(y * i + (n - 3 * i) * x)
    
    print(min(ans))

if __name__ == "__main__":
    main()