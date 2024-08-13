'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc351/tasks/abc351_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc351/tasks/abc351_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline

from collections import deque

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    q = deque()
    l = 0
    for i in range(n):
        q.append(a[i])
        l += 1
        while len(q) > 1 and q[-1] == q[-2]:
            q.pop()
            q[-1] += 1
    
    print(len(q))


if __name__ == "__main__":
    main()