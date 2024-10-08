'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc356/tasks/abc356_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/abc356/tasks/abc356_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N, L, R = map(int, input().split())
    A = []
    for i in range(1, L):
        A.append(i)
    for i in reversed(range(L, R + 1)):
        A.append(i)
    for i in range(R + 1, N + 1):
        A.append(i)
    
    print(*A)


if __name__ == "__main__":
    main()