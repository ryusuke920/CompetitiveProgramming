'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc355/tasks/abc355_b
oj t -c "python3 B.py"
oj s https://atcoder.jp/contests/abc355/tasks/abc355_b B.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def main() -> None:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append(A[i])
    for i in range(M):
        C.append(B[i])
    C.sort()
    for i in range(N + M - 1):
        if C[i] in A and C[i + 1] in A:
            exit(print("Yes"))
    
    print("No")


if __name__ == "__main__":
    main()