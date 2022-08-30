'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc264/tasks/abc264_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc264/tasks/abc264_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''


"""
BITを行った後の数列は昇順になるので注意！
"""
import copy

def BIT(A: list) -> int:
    "転倒数を求める"
    cnt = 0
    n = len(A)
    if n > 1:
        A1 = A[: n >> 1]
        A2 = A[n >> 1 :]
        cnt += BIT(A1)
        cnt += BIT(A2)
        i1, i2 = 0, 0
        for i in range(n):
            if i2 == len(A2):
                A[i] = A1[i1]
                i1 += 1
            elif i1 == len(A1):
                A[i] = A2[i2]
                i2 += 1
            elif A1[i1] <= A2[i2]:
                A[i] = A1[i1]
                i1 += 1
            else:
                A[i] = A2[i2]
                i2 += 1
                cnt += n // 2 - i1
    return cnt

from collections import defaultdict

def main() -> None:
    d = defaultdict(int)
    for i, j in enumerate('atcoder'):
        d[j] = i

    print(BIT([d[i] for i in input()]))

if __name__ == "__main__":
    main()