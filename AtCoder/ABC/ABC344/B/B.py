'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc344/tasks/abc344_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc344/tasks/abc344_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    ans = []
    while True:
        n = int(input())
        ans.append(n)
        if n == 0:
            break
    print(*ans[::-1], sep="\n")

if __name__ == "__main__":
    main()