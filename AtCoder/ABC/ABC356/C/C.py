'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc356/tasks/abc356_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc356/tasks/abc356_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from itertools import product

def main() -> None:
    N, M, K = map(int, input().split())
    A = []
    S = ""
    for i in range(M):
        T = list(input().split())
        a = []
        for j in range(int(T[0])):
            a.append(int(T[j + 1]))
        A.append(a)
        S += T[-1]
    l = []
    for i in range(M):
        l.append(len(A[i]))

    ans = 0
    for bit in product([0, 1], repeat=N):
        flag = True
        for i in range(M):
            num = 0
            for j in range(l[i]):
                if bit[A[i][j] - 1] == 1:
                    num += 1
            if num >= K and S[i] == "x":
                flag = False
            if num < K and S[i] == "o":
                flag = False
        if flag:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()