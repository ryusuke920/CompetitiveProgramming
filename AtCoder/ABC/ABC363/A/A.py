'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc363/tasks/abc363_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc363/tasks/abc363_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    R = int(input())
    ans = 0
    for i in range(1000):
        R += 1
        ans += 1
        if R % 100 == 0:
            exit(print(ans))

if __name__ == "__main__":
    main()