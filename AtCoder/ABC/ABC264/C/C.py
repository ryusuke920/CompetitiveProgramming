'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc264/tasks/abc264_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc264/tasks/abc264_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

from itertools import product

def main() -> None:
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    p, q = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(p)]

    for i in product([0, 1], repeat=h):
        for j in product([0, 1], repeat=w):
            num = []

            for ii in range(h):
                if i[ii] == 0:
                    continue
                num_ = []
                for jj in range(w):
                    if i[ii] and j[jj]:
                        num_.append(a[ii][jj])
                num.append(num_)
                
            if b == num:
                exit(print('Yes'))
    
    print('No')


if __name__ == "__main__":
    main()