'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc365/tasks/abc365_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc365/tasks/abc365_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append((A[i], i + 1))
    B.sort(reverse=True, key=lambda x: x[0])
    print(B[1][1])

if __name__ == "__main__":
    main()