'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc331/tasks/abc331_c
oj t -c "python3 C.py"
oj s https://atcoder.jp/contests/abc331/tasks/abc331_c C.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    b = [a[i] for i in range(n)]
    b.sort()
    for i in range(n):
        s[i + 1] += s[i] + b[i]
    # print(s)
    # print(b)
    sum_ = sum(a)
    ans = []
    for i in range(n):
        t = bisect_right(b, a[i])
        #print(t)
        ans.append(sum_ - s[t])
    print(*ans)



if __name__ == "__main__":
    main()