'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/arc179/tasks/arc179_a
oj t -c "python3 A.py"
oj s https://atcoder.jp/contests/arc179/tasks/arc179_a A.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

def plus() -> None:
    A.sort()
    S = [0]*(N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    flag = False
    for i in range(N + 1):
        if S[i] >= K:
            flag = True
            if flag and S[i] < K:
                exit(print("No"))

    print("Yes")
    print(*A)


def minus() -> None:
    A.sort(reverse=True)
    S = [0]*(N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    flag = False
    for i in range(N + 1):
        if S[i] >= K:
            flag = True
        if flag and S[i] < K:
            exit(print("No"))
    
    print("Yes")
    print(*A)


N, K = map(int, input().split())
A = list(map(int, input().split()))
if K > 0:
    plus()
else:
    minus()