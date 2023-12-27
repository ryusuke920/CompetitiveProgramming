'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc318/tasks/abc318_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc318/tasks/abc318_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    n, m, p = map(int, input().split())
    ans = 0
    for i in range(m, 10**6, p):
        if i <= n:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()