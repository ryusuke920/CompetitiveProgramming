'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc348/tasks/abc348_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc348/tasks/abc348_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n = int(input())
    x, y = [0] * n, [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())

    for i in range(n):
        d = 0
        ans = 0
        for j in range(n):
            dy = y[i] - y[j]
            dx = x[i] - x[j]
            p = dx**2 + dy**2
            if p > d:
                d = p
                ans = j
        
        print(ans + 1)


if __name__ == "__main__":
    main()